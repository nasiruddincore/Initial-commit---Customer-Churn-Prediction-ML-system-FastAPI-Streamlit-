import streamlit as st
import requests

st.set_page_config(page_title="Churn Dashboard", layout="wide")

API_URL = "http://127.0.0.1:8000/predict"

st.title("📊 Customer Churn Prediction Dashboard")

# =========================
# INPUTS
# =========================
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure", 0, 72, 12)

internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# =========================
# PREDICT
# =========================
if st.button("Predict Churn"):

    payload = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": internet,
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": contract,
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()

        if result["churn"] == 1:
            st.error("⚠️ Customer will CHURN")
        else:
            st.success("✅ Customer will STAY")

    except Exception as e:
        st.error(f"API Error: {e}")