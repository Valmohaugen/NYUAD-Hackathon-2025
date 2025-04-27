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

1. **Dataset 1:** [Link to Data ](https://www.kaggle.com/datasets/danielesayuriono/eeg-signals-for-anxiety-levels-detection)  
   *(Anxiety Dataset 01)*  

2. **Dataset 2:** [Link to Paper 2](https://zenodo.org/records/13690792)  
   *(Anxiety Dataset 02)*  

---

## Results  
| **Model**           | **Anxiety AUC** | **Depression AUC** |  **Anxiety Accuracy**  | **Depression Accuracy**|  
|----------------------|-----------------|--------------------|------------------------|------------------------|  
| **Classical Models** |  68%            |  68%               |  38%                   |  69%                   |  
| **QSVM**             | **79%**         | **73%**            | **81%**                | **70%**                |  

✅ Our performance findings demonstrate the **superiority of quantum-enhanced models**, underlining their potential for impactful applications in mental health diagnostics.  

---  

## Brain Waves Mental Health Analyzer  

**Brain Waves Mental Health Analyzer** is a Streamlit web app that uses brain wave analysis to predict mental health conditions and provides compassionate, personalized advice using OpenAI GPT-4.  

### Features  

- 🎯 **Accurate Analysis**: Classifies brainwave results across depression, anxiety, schizophrenia, ADHD, and normal brain health.  
- 📊 **Interactive Visualizations**: Displays mental health likelihoods using beautiful pie charts.  
- 💬 **Caring AI Chatbot**: Users can chat with a support bot for emotional assistance.  
- 🧘‍♂️ **Personalized Self-Care Tips**: Recommends helpful advice based on the user’s situation.  
- 🏥 **Easy Sharing**: Allows users to share results with doctors or family, or save for later.  
- 🔒 **Privacy First**: No sensitive data storage; real-time analysis on your device.  

Website: https://neurotiq.vercel.app/

### Installation  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/yourusername/brainwave-mental-health-analyzer.git
   cd brainwave-mental-health-analyzer
   ```  

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Set your OpenAI API key**:  
   - On Linux/macOS:  
     ```bash
     export OPENAI_API_KEY="your-openai-api-key"
     ```  
   - On Windows CMD:  
     ```cmd
     set OPENAI_API_KEY=your-openai-api-key
     ```  

4. **Run the app**:  
   ```bash
   streamlit run disease_checker_app1.py
   ```  

### Usage  

- Click **Receive New Data** to simulate brain wave test results.  
- Click **Analyze Data** to get warm, easy-to-understand analysis.  
- Review **Self-Care Tips** generated just for you.  
- Chat live with the **Support Bot** for emotional support.  
- Find nearby mental health services or share your report securely.  

### Requirements  

- Python 3.8+  
- Packages:  
  - streamlit  
  - pandas  
  - altair  
  - langchain  
  - langchain-openai  
  - openai  

(installable using `pip install -r requirements.txt`)  

### Project Structure  

- `disease_checker_app1.py` – Main Streamlit app.  
- `requirements.txt` – Dependency list.  
- `README.md` – Project overview and instructions.  

---  

## About the Team  
We are **Team NeurotiQ**, a passionate group of innovators from NYU Abu Dhabi, united by our commitment to advancing mental health solutions through cutting-edge technology.
