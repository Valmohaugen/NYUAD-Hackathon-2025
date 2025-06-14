import os
import torch
import numpy as np
import scipy.io
import mne
from pathlib import Path
from torch.utils.data import Dataset

class AMIGOS(Dataset):
    def __init__(
        self,
        root: str,
        label_type: str = "A",  # "A" for arousal, "V" for valence
        ground_truth_threshold: float = 5.0,
        preprocessed: bool = True,
        transform = None
    ):
        self.root = Path(root) / Path("Physiological Recordings") / Path("Matlab Preprocessed Data" if preprocessed else "Matlab Original Data")
        self.label_type = label_type
        self.ground_truth_threshold = ground_truth_threshold
        self.transform = transform
        self.preprocessed = preprocessed
        
        # EEG setup - create once and reuse
        self.info = mne.create_info(
            ["AF3", "F7", "F3", "FC5", "T7", "P7", "O1", "O2", "P8", "T8",
             "FC6", "F4", "F8", "AF4", "ECG_Right", "ECG_Left", "GSR"],
            128, ch_types="eeg"
        )
        
        # Cache for loaded data
        self._data_cache = {}
        self._label_cache = {}
        
        # Load all data at initialization
        self._load_all_data()
    
    def _load_all_data(self):
        """Load and cache all data for efficient access"""
        for subject_id in range(1, 41):
            try:
                data, labels = self._load_subject(subject_id)
                self._data_cache.update(data)
                self._label_cache.update(labels)
            except Exception as e:
                print(f"Error loading subject {subject_id}: {e}")
    
    def _load_subject(self, subject_id):
        """Load data for a single subject efficiently"""
        file_name = f"Data_Preprocessed_P{subject_id:02d}.mat" if self.preprocessed else f"Data_Original_P{subject_id}.mat"
        data = scipy.io.loadmat(os.path.join(self.root, file_name))
        data = data["joined_data"][0]
        labels = data["labels_selfassessment"][0]
        
        data_dict, label_dict = {}, {}
        for i in range(min(16, data.shape[0])):
            # Process EEG data efficiently
            eeg_data = mne.io.RawArray(data[i].T, self.info)
            if self.transform:
                eeg_data = self.transform(eeg_data)
            data_dict[i] = np.expand_dims(eeg_data.get_data(), axis=-3)
            label_dict[i] = np.array([labels[i][0][0], labels[i][0][1]])  # [arousal, valence]
            
        return data_dict, label_dict
    
    def __get_subject_ids__(self):
        """Return list of subject IDs"""
        return list(range(1, 41))
    
    def __get_subject__(self, subject_id):
        """Get cached data for a specific subject"""
        if subject_id not in self._data_cache:
            data, labels = self._load_subject(subject_id)
            self._data_cache.update(data)
            self._label_cache.update(labels)
        return self._data_cache, self._label_cache
    
    def __getitem__(self, index):
        """Get a single data point from cache"""
        return torch.from_numpy(self._data_cache[index]), torch.tensor(self._label_cache[index])
    
    def __len__(self):
        """Get total number of samples"""
        return len(self._data_cache)