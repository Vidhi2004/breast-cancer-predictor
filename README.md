# 🔬 Breast Cancer Detection Web App

This is a machine learning-powered web application that predicts whether a tumor is **benign** or **malignant** based on user-provided medical features. Built with Flask and trained using the Breast Cancer Wisconsin dataset.

---

## 🧠 Features

- Predicts tumor classification: `Malignant` or `Benign`
- Clean and intuitive user interface using Bootstrap
- Accepts 10 input features from the dataset
- Displays prediction with a visual message
- Includes sample values for both malignant and benign cases
- Future-ready: supports deployment and extensions

---

## 📊 Input Features Used

1. Radius Mean  
2. Texture Mean  
3. Perimeter Mean  
4. Area Mean  
5. Smoothness Mean  
6. Compactness Mean  
7. Concavity Mean  
8. Concave Points Mean  
9. Symmetry Mean  
10. Fractal Dimension Mean  

---

## 💻 Technologies Used

- Python
- Flask
- Scikit-learn
- HTML5 + CSS3 (Bootstrap)
- Google Colab (for model training)

---

## 🧪 Model Details

- Algorithm: `RandomForestClassifier`
- Trained on: Breast Cancer Wisconsin (Diagnostic) dataset
- Accuracy: ~95% (varies depending on train-test split)

---

## 📁 Project Structure

├── app.py # Flask backend
├── model.pkl # Trained ML model
├── templates/
│ └── index.html # UI for inputs
├── static/
│ └── ui-screenshot.png # Screenshot of the app (add your image here)
├── requirements.txt # Python dependencies
└── README.md # Project overview

---

## 🛠️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/breast-cancer-predictor.git
   cd breast-cancer-predictor

2. Create a virtual environment and install requirements:
     ```bash
    pip install -r requirements.txt

3. Run the Flask app:
    ```bash
    python app.py

4. Open your browser and navigate to:
    ```bash
    http://localhost:5000

---
# ✅ Output
Once you enter the values, the app will classify the tumor as either:

🟢 Benign (Non-cancerous)
🔴 Malignant (Cancerous)

---
# Sample Inputs (for testing)
✅ Benign Example:
    ```bash 
    Radius Mean: 12.02
    Texture Mean: 14.53
    Perimeter Mean: 78.3
    Area Mean: 449.3
    Smoothness Mean: 0.1022
    Compactness Mean: 0.1453
    Concavity Mean: 0.1059
    Concave Points Mean: 0.053
    Symmetry Mean: 0.1928
    Fractal Dimension Mean: 0.0641


❌ Malignant Example:
    ```bash
    Radius Mean: 17.99
    Texture Mean: 10.38
    Perimeter Mean: 122.8
    Area Mean: 1001.0
    Smoothness Mean: 0.1184
    Compactness Mean: 0.2776
    Concavity Mean: 0.3001
    Concave Points Mean: 0.1471
    Symmetry Mean: 0.2419
    Fractal Dimension Mean: 0.0787