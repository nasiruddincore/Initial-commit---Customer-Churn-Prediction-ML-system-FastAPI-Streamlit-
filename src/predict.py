import joblib
import pandas as pd

model = joblib.load("models/churn_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

def predict(data: dict):
    df = pd.DataFrame([data])
    df = preprocessor.transform(df)
    prediction = model.predict(df)[0]
    return int(prediction)