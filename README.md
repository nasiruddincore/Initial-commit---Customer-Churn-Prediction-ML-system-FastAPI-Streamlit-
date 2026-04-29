# 📊 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts customer churn using a Telco-style dataset. This project demonstrates a complete ML pipeline including data generation, preprocessing, model training, API deployment, and an interactive dashboard.

---

## 🚀 Features

- 📁 Synthetic Telco Dataset (Kaggle-style)
- 🔧 Data Preprocessing Pipeline
- 🤖 Random Forest ML Model
- ⚡ FastAPI Backend (Real-time Prediction)
- 📊 Streamlit Dashboard (User Interface)
- 🔗 End-to-End Integration

---

## 🧠 Problem Statement

Customer churn is a critical issue for businesses. This project predicts whether a customer will leave a service based on usage patterns and demographics, helping companies take proactive retention actions.

---

## 🏗️ Project Structure


Customer-Churn-Prediction/
│
├── app/
│ ├── api.py
│ └── streamlit_app.py
│
├── data/
│ └── churn.csv
│
├── models/
│ ├── churn_model.pkl
│ └── preprocessor.pkl
│
├── src/
│ ├── train.py
│ ├── preprocessing.py
│ ├── predict.py
│ └── utils.py
│
├── create_telco_dataset.py
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1. Clone the Repository

git clone https://github.com/nasiruddincore/customer-churn-prediction.git

cd customer-churn-prediction


### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate # Windows


### 3. Install Dependencies

pip install -r requirements.txt


---

## ▶️ How to Run the Project

### Step 1: Generate Dataset

python create_telco_dataset.py


### Step 2: Train Model

python -m src.train


### Step 3: Start FastAPI Server

uvicorn app.api:app --reload


Open:

http://127.0.0.1:8000/docs


### Step 4: Run Streamlit Dashboard

streamlit run app/streamlit_app.py


---

## 📊 Dashboard Preview

- Input customer details
- Predict churn in real-time
- Simple UI for business users

---

## 🧪 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Joblib

---

## 📈 Model Details

- Algorithm: Random Forest Classifier
- Task: Binary Classification (Churn / No Churn)
- Input Features: Demographics, Services, Billing
- Output: Churn Prediction (0 or 1)

---

## 🎯 Use Cases

- Customer retention strategies
- Targeted marketing campaigns
- Business analytics dashboards
- Real-time churn monitoring

---

## 🔥 Future Improvements

- SHAP Explainability
- Hyperparameter Tuning
- Deployment on AWS / Render
- Docker Integration
- Next.js Frontend

---

## 👨‍💻 Author

Nasir Uddin

---

## ⭐ If you like this project, give it a star!
