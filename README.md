# 🧠 NeurotiQ — Quantum Machine Learning for EEG Signal Analysis
**NYUAD Social Impact Hackathon 2025**

## Overview
NeurotiQ is focused on applying **Quantum Machine Learning (QML)** to improve EEG signal analysis for mental health diagnosis, specifically depression and anxiety detection.  
We are exploring how quantum-enhanced models can better capture complex EEG patterns compared to classical machine learning models.

Our models are implemented in **Python** using:
- **Quantum Libraries**: `Qiskit`, `PennyLane`
- **Classical Libraries**: `Scikit-learn`, `TensorFlow`, `Pandas`, `NumPy`, etc.  
  *(Full list of required packages can be installed via pip, see `requirements.txt`.)*

## Models
We have currently developed and tested **four models**:
- **2 Classical models** (baseline)
- **2 Quantum-enhanced models** (our main focus)

### Classical Models
- **Classical SVM** (Support Vector Machine)
- **Classical Neural Network**

### Quantum Models
- **Quantum CNN (QCNN):**  
  - EEG features are mapped into quantum states via **amplitude encoding**.
  - **Strongly entangling layers** are applied to transform the quantum states.
  - A **hybrid classical-quantum** model structure is used: quantum feature extraction followed by classical classification layers.

- **Quantum SVM (QSVM):**  
  - EEG data is embedded into quantum states using **quantum circuits**.
  - A **quantum kernel** is computed based on quantum state overlaps.
  - A classical SVM is trained using the **quantum-enhanced kernel** for improved separability.

## Results
| Model | Anxiety AUC | Depression AUC |
|:-----:|:-----------:|:--------------:|
| Classical Models | ~49% | ~49% |
| **QSVM (Quantum SVM)** | **79%** | **73%** |

✅ The quantum-enhanced models **significantly outperform** classical models, demonstrating the potential of quantum computing for real-world mental health applications.

---

## Installation
```bash
pip install -r requirements.txt
```

Main packages used:
- `qiskit`
- `pennylane`
- `tensorflow`
- `scikit-learn`
- `pandas`
- `numpy`

(See `requirements.txt` for full list.)

## Team
**Team NeurotiQ** — NYU Abu Dhabi, Social Impact Hackathon 2025
