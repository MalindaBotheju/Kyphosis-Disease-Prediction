# 🩺 Kyphosis Disease Prediction: End-to-End ML Solution

An AI-powered medical screening tool designed to predict the presence of Kyphosis deformity in pediatric patients following spinal surgery. This project bridges the gap between raw data science and a functional medical dashboard.

## 📊 Project Performance
Our Tuned SVM model was specifically optimized for **medical safety** by prioritizing Recall over simple Accuracy:

* **Recall (Medically Critical):** 75% for 'Present' cases — ensuring fewer sick patients are missed.
* **Accuracy:** 76%.
* **Dataset:** 81 clinical patient records.

---

## 🖥️ User Interface & Experience
The application features a modern, responsive dashboard built with **Flask** and **Tailwind CSS**.

| Patient Screening (Input) | Prediction Result (Output) |
| :--- | :--- |
| ![Screening UI](https://raw.githubusercontent.com/MalindaBotheju/Kyphosis-Disease-Prediction/master/static/normal_detection.png) | ![Result UI](https://raw.githubusercontent.com/MalindaBotheju/Kyphosis-Disease-Prediction/master/static/detection.png) |

> **Persistence Feature:** The dashboard is designed to retain user input after prediction, allowing medical staff to quickly adjust variables without re-typing data.

---

## 🛠️ Technical Stack & Files
* **Core:** Python, Scikit-Learn, Pandas, Numpy
* **Backend:** Flask
* **Frontend:** HTML5, Tailwind CSS (via CDN)
* **Model Deployment:** Joblib serialization

### Repository Structure
- `app.py`: The Flask server and prediction logic.
- `kyphosis_svm_model.pkl`: The "Brain" (Tuned SVM Model).
- `kyphosis_scaler.pkl`: The "Translator" (StandardScaler).
- `kyphosis.ipynb`: The complete research, EDA, and model tuning notebook.
- `templates/` & `static/`: Frontend assets and medical diagrams.

---

## 🚀 Installation & Local Deployment
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/MalindaBotheju/Kyphosis-Disease-Prediction.git](https://github.com/MalindaBotheju/Kyphosis-Disease-Prediction.git)