# 🧠 NeurotiQ — Quantum Machine Learning for EEG Signal Analysis  
**NYUAD Social Impact Hackathon 2025**  

---

## Overview  
NeurotiQ leverages **Quantum Machine Learning (QML)** algorithms to enhance EEG signal analysis, revolutionizing mental health diagnosis for conditions such as depression, ADHD, and anxiety.  

Our focus is on demonstrating how quantum-enhanced models can uncover intricate EEG patterns that classical machine learning models struggle to identify.  

**Core technologies:**  
- **Quantum Libraries:** `Qiskit`, `PennyLane`  
- **Classical Libraries:** `Scikit-learn`, `TensorFlow`, `Pandas`, `NumPy`, etc.  

---  

## Models  
We have developed and rigorously tested **four models** to date:  
- **2 Classical models** (baseline for comparison)  
- **2 Quantum-enhanced models** (our innovative approach)  

### Classical Models  
1. **Support Vector Machine (SVM):** A traditional method for classification tasks.  
2. **Regression models:** A logistic regression approach trained on EEG features.  

### Quantum Models  
1. **Quantum Neural Network (QNN):**  
   - EEG data is transformed into quantum states using **amplitude encoding**.  
   - **Strongly entangling layers** are applied to exploit quantum correlations.  
   - Combines **quantum feature extraction** with classical classification layers for a hybrid approach.  

2. **Quantum Support Vector Machine (QSVM):**  
   - EEG features are embedded into quantum states using **amplitude encoding**.  
   - A **quantum kernel** is calculated by analyzing quantum state overlaps.  
   - Enhanced separability is achieved by training a SVC with the quantum kernel.  

---  

## Datasets  
The datasets used for this project are sourced from the following studies:  

1. **Dataset 1:** [Link to Paper 1](#)  
   *(Brief description of what this dataset includes and how it supports the research, e.g., EEG signals associated with mental health conditions.)*  

2. **Dataset 2:** [Link to Paper 2](#)  
   *(Brief description of what this dataset includes, focusing on its relevance to the study.)*  

---

## Results  
| **Model**           | **Anxiety AUC** | **Depression AUC** |  **Anxiety Accuracy**  | **Depression Accuracy**|  
|----------------------|-----------------|--------------------|------------------------|------------------------|  
| **Classical Models** | ~49%            | ~49%               | ~39%                   | ~69%                   |  
| **QSVM**             | **79%**         | **73%**            | ~81%                   | ~70%                   |  

✅ Our performance findings demonstrate the **superiority of quantum-enhanced models**, underlining their potential for impactful applications in mental health diagnostics.  

---  

## Installation  
1. Clone the repository.  
2. Install dependencies using the following command:  
   ```bash  
   pip install qiskit pennylane tensorflow scikit-learn pandas numpy  
   ```  

**Key libraries include:**  
- `qiskit`  
- `pennylane`  
- `tensorflow`  
- `scikit-learn`  
- `pandas`  
- `numpy`  

---

## About the Team  
We are **Team NeurotiQ**, a passionate group of innovators from NYU Abu Dhabi, united by our commitment to advancing mental health solutions through cutting-edge technology.
