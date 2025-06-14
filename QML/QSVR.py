import numpy as np
from sklearn.metrics import (
    f1_score, accuracy_score, recall_score, precision_score, 
    classification_report
)
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import DiagonalGate, Initialize

# from eegain.data.datasets import AMIGOS

def extract_features(eeg):
    """Extract mean and standard deviation features from EEG data efficiently"""
    return np.concatenate([np.mean(eeg, axis=1), np.std(eeg, axis=1)])

def get_amigos_data_for_classification(
    root, label_type="A", ground_truth_threshold=5, max_subjects=None
):
    """
    Load and preprocess AMIGOS dataset for classification
    
    Args:
        root: Path to AMIGOS dataset
        label_type: "A" for arousal or "V" for valence
        ground_truth_threshold: Threshold for binary classification
        max_subjects: Maximum number of subjects to include (None for all)
    
    Returns:
        X: Feature matrix (n_samples, n_features)
        y: Binary labels (n_samples,)
    """
    dataset = AMIGOS(
        root=root,
        label_type=label_type,
        ground_truth_threshold=ground_truth_threshold,
        preprocessed=True,  # Use preprocessed data for efficiency
        transform=None
    )
    
    # Pre-allocate lists for better memory efficiency
    all_X = []
    all_y = []
    
    # Get subject IDs and limit if specified
    subject_ids = dataset.__get_subject_ids__()[:max_subjects] if max_subjects else dataset.__get_subject_ids__()
    
    # Process each subject
    for subject_id in subject_ids:
        try:
            data, labels = dataset.__get_subject__(subject_id)
            for trial_idx, eeg in data.items():
                # Extract features efficiently
                features = extract_features(eeg.squeeze(0) if eeg.ndim == 3 else eeg)
                all_X.append(features)
                
                # Process label
                label = labels[trial_idx][0 if label_type == "A" else 1]
                all_y.append(0 if label <= ground_truth_threshold else 1)
        except Exception as e:
            print(f"Skipping subject {subject_id} due to error: {e}")
    
    return np.array(all_X), np.array(all_y)

# ---- Quantum Kernel Section ----

def get_quantum_kernel(num_qubits):
    """
    Create a quantum kernel function for quantum SVM
    
    Args:
        num_qubits: Number of qubits to use in the quantum circuit
    
    Returns:
        build_kernel_matrix: Function that computes the quantum kernel matrix
    """
    def feature_map_circuit(x):
        """Create quantum circuit for feature mapping"""
        qr = QuantumRegister(num_qubits)
        qc = QuantumCircuit(qr)
        
        # Normalize and pad input
        x_norm = x / np.linalg.norm(x)
        x_pad = np.zeros(2**num_qubits)
        x_pad[:min(len(x_norm), 2**num_qubits)] = x_norm[:min(len(x_norm), 2**num_qubits)]
        
        # Amplitude encoding
        qc.append(Initialize(x_pad), qr)
        
        # Phase encoding
        phases = np.mod(x_pad, 2 * np.pi)
        diag = np.exp(1j * phases)
        qc.append(DiagonalGate(diag), qr)
        
        return transpile(qc, basis_gates=['u3', 'cx'])

    def quantum_kernel(x1, x2):
        """Compute quantum kernel between two feature vectors"""
        sv1 = Statevector.from_instruction(feature_map_circuit(x1))
        sv2 = Statevector.from_instruction(feature_map_circuit(x2))
        return np.abs(np.vdot(sv1.data, sv2.data))**2

    def build_kernel_matrix(A, B):
        """Build kernel matrix efficiently using vectorized operations where possible"""
        return np.array([[quantum_kernel(a, b) for b in B] for a in A])
    
    return build_kernel_matrix

# ---- Main Script ----

if __name__ == "__main__":
    # Configuration
    data_root = "/path/to/AMIGOS"
    label_type = "A"  # "A" for arousal, "V" for valence
    ground_truth_threshold = 5
    num_qubits = 2  # Number of qubits for quantum circuit
    
    # Load and preprocess data
    print("Loading AMIGOS dataset...")
    X, y = get_amigos_data_for_classification(
        data_root, 
        label_type=label_type, 
        ground_truth_threshold=ground_truth_threshold
    )
    
    # Pad/trim features to match quantum circuit size
    feature_len = 2**num_qubits
    X = np.pad(X, ((0, 0), (0, max(0, feature_len - X.shape[1]))))[:, :feature_len]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Build and compute quantum kernel
    print(f"Building quantum kernel with {num_qubits} qubits...")
    build_kernel_matrix = get_quantum_kernel(num_qubits)
    K_train = build_kernel_matrix(X_train, X_train)
    K_test = build_kernel_matrix(X_test, X_train)
    
    # Train and evaluate
    print("Training quantum SVM...")
    clf = SVC(kernel='precomputed')
    clf.fit(K_train, y_train)
    y_pred = clf.predict(K_test)
    
    # Print metrics
    print("\nModel Performance:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred, average="binary"))
    print("Precision:", precision_score(y_test, y_pred, average="binary"))
    print("F1 score:", f1_score(y_test, y_pred, average="binary"))
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred))