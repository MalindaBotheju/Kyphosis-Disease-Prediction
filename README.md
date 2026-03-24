# 🩺 Kyphosis Disease Prediction AI

## 📌 Project Overview
This project applies a **Tuned Support Vector Machine (SVM)** classifier to clinical data. The goal is to assist medical professionals in post-operative screening. Unlike standard models, this was optimized for **medical safety**, prioritizing the detection of actual cases (Recall) over simple accuracy.

### 🧪 Medical Comparison
| Normal Spine | Kyphotic Deformity |
| :---: | :---: |
| ![Normal](static/normal.png) | ![Kyphosis](static/kyphosis.png) |
| *Expected post-op alignment* | *Post-op complications detected* |

---

## 🖥️ Dashboard UI
The application provides a real-time interface for screening.

| Case: No Kyphosis Detected | Case: Kyphosis Detected |
| :--- | :--- |
| ![Normal Result](static/normal_detection.png) | ![Detected Result](static/detection.png) |

---

## 📊 Model Performance
* **Recall (Sensitivity):** 75% — *Optimized to ensure 3 out of 4 positive cases are caught.*
* **Accuracy:** 76% 
* **Model Type:** Support Vector Machine (RBF Kernel)
* **Scaling:** StandardScaler (Z-score normalization)

---

## 🛠️ Repository Structure
- `app.py`: Flask backend and prediction API.
- `kyphosis_svm_model.pkl`: Pre-trained SVM "Brain".
- `kyphosis_scaler.pkl`: Input "Translator".
- `kyphosis.ipynb`: Full EDA, Data Cleaning, and Model Training history.
- `requirements.txt`: List of dependencies for deployment.
