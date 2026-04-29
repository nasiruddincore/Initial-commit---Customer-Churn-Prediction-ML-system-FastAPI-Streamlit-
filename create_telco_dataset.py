import pandas as pd
import numpy as np
import os

# =========================
# CREATE DATA FOLDER
# =========================
os.makedirs("data", exist_ok=True)

np.random.seed(42)
n = 2000

# =========================
# BASIC CUSTOMER INFO
# =========================
customerID = [f"CUST_{i:05d}" for i in range(n)]
gender = np.random.choice(["Male", "Female"], n)
SeniorCitizen = np.random.choice([0, 1], n, p=[0.8, 0.2])
Partner = np.random.choice(["Yes", "No"], n)
Dependents = np.random.choice(["Yes", "No"], n)

# =========================
# SERVICE INFO
# =========================
tenure = np.random.randint(1, 72, n)
PhoneService = np.random.choice(["Yes", "No"], n, p=[0.9, 0.1])
MultipleLines = np.random.choice(["Yes", "No", "No phone service"], n)

InternetService = np.random.choice(["DSL", "Fiber optic", "No"], n, p=[0.4, 0.4, 0.2])

OnlineSecurity = np.random.choice(["Yes", "No", "No internet service"], n)
OnlineBackup = np.random.choice(["Yes", "No", "No internet service"], n)
DeviceProtection = np.random.choice(["Yes", "No", "No internet service"], n)
TechSupport = np.random.choice(["Yes", "No", "No internet service"], n)
StreamingTV = np.random.choice(["Yes", "No", "No internet service"], n)
StreamingMovies = np.random.choice(["Yes", "No", "No internet service"], n)

Contract = np.random.choice(["Month-to-month", "One year", "Two year"], n, p=[0.6, 0.25, 0.15])
PaperlessBilling = np.random.choice(["Yes", "No"], n, p=[0.7, 0.3])
PaymentMethod = np.random.choice([
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
], n)

# =========================
# FINANCIAL FEATURES
# =========================
MonthlyCharges = np.round(np.random.uniform(20, 120, n), 2)
TotalCharges = np.round(MonthlyCharges * tenure + np.random.normal(0, 50, n), 2)

# =========================
# REALISTIC CHURN LOGIC
# =========================
risk = (
    (tenure < 12) * 0.35 +
    (Contract == "Month-to-month") * 0.25 +
    (InternetService == "Fiber optic") * 0.15 +
    (MonthlyCharges > 80) * 0.15 +
    (SeniorCitizen == 1) * 0.10
)

prob = 1 / (1 + np.exp(-3 * (risk - 0.5)))
Churn = np.where(np.random.rand(n) < prob, "Yes", "No")

# =========================
# CREATE DATAFRAME (KAGGLE STYLE)
# =========================
df = pd.DataFrame({
    "customerID": customerID,
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "Churn": Churn
})

# =========================
# SAVE FILE
# =========================
file_path = "data/churn.csv"
df.to_csv(file_path, index=False)

print("✅ Kaggle-style Telco dataset created successfully!")
print("📁 Saved at:", file_path)
print(df.head())