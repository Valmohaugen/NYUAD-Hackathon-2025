# NYUAD Hackathon 2025: NeurotiQ

This repository is the home for NeurotiQ, a quantum machine learning pipeline for EEG-based mental health diagnosis, combining QSVM and QCNN models with classical baselines and a GPT-4-powered Streamlit web app for interactive brain wave analysis.

## Features

- **Quantum Support Vector Machine (QSVM):**
  Qiskit-based quantum kernel SVM with amplitude embedding and diagonal phase encoding for anxiety and depression classification from EEG data. Achieves 79% AUC on anxiety detection.

- **Quantum Convolutional Neural Network (QCNN):**
  PennyLane + TensorFlow hybrid QCNN using StronglyEntanglingLayers for EEG-based diagnosis benchmarking.

- **Classical ML Baselines:**
  SVM, logistic regression, and AutoML (PyCaret) ensemble methods for comparison against quantum approaches.

- **Brain Wave Analyzer App:**
  Streamlit web app with GPT-4 integration for interactive EEG analysis, personalized recommendations, severity classification, and an emotional support chatbot.

- **Multiple EEG Datasets:**
  Anxiety, depression, and ADHD datasets with preprocessing pipelines (KNN imputation, PCA dimensionality reduction, L2 normalization).

## Project Structure

```
NYUAD-Hackathon-2025/
  README.md
  requirements.txt                    # All project dependencies
  .gitignore
  ClassicalML/                        # Classical ML baseline notebooks
    Anxiety_Detection_classical_model_01.ipynb
    Anxiety_Detection_classical_model_02.ipynb
  QML/                                # Quantum ML notebooks
    QSVMAnxiety.ipynb                 # QSVM for anxiety detection (main model)
    QSVMdepression.ipynb              # QSVM for depression detection
    QCNNanxiety.ipynb                 # QCNN for anxiety detection
    QCNNdepression.ipynb              # QCNN for depression detection
    svm_model.pkl                     # Trained QSVM model
  Datasets/                           # EEG datasets
    Anxiety_DataSet_EEG.xlsx
    Depression_DataSet_EEG.csv
    EEG.machinelearing_data_BRMH.csv
    Anxiety_split/                    # PCA-reduced train/test splits (.npy)
    ADHD_in_children_dataset/         # ADHD EEG recordings (.mat)
  Recommendation_System/              # Streamlit web app
    Recommendation_System.py
    requirements.txt
  docs/                               # Internal hackathon docs
    To_Do.md
    Resources.md
  NeurotiQ.png
  Team_NeurotiQ.png
  NYUAD-QC-Hackathon-NeurotiQ-Presentation.pdf
```

## How to Use This Repository

Clone the repository:

```bash
git clone https://github.com/Valmohaugen/NYUAD-Hackathon-2025.git
cd NYUAD-Hackathon-2025
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the quantum ML notebooks:

```bash
jupyter notebook QML/QSVMAnxiety.ipynb
```

Run the Streamlit app (requires an OpenAI API key):

```bash
export OPENAI_API_KEY="your-api-key-here"
cd Recommendation_System
streamlit run Recommendation_System.py
```

Or visit the deployed version: [neurotiq.vercel.app](https://neurotiq.vercel.app/)

## Results

| Model            | Anxiety (AUC / Accuracy) | Depression (AUC / Accuracy) |
|------------------|--------------------------|------------------------------|
| Classical SVM    | 68% / 38%                | 68% / 69%                    |
| **Quantum QSVM** | **79% / 81%**           | **73% / 70%**                |

## Datasets

| Dataset | Source | Used For |
|---------|--------|----------|
| Anxiety EEG | [Kaggle](https://www.kaggle.com/datasets/danielesayuriono/eeg-signals-for-anxiety-levels-detection) | QSVM/QCNN anxiety classification |
| Depression EEG | [Zenodo](https://zenodo.org/records/13690792) | QSVM/QCNN depression classification |
| ADHD EEG | Included in `Datasets/ADHD_in_children_dataset/` | Future work |

## Dependencies

Python 3.10+, PennyLane, Qiskit, qiskit-aer, TensorFlow, scikit-learn, XGBoost, NumPy, Pandas, SciPy, Matplotlib, Streamlit, LangChain, OpenAI, Altair

See `requirements.txt` for the full list.
