import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from src.preprocessing import Preprocessor

BASE = os.path.dirname(os.path.dirname(__file__))

DATA_PATH = os.path.join(BASE, "data", "churn.csv")
MODEL_PATH = os.path.join(BASE, "models", "churn_model.pkl")
PREPROCESSOR_PATH = os.path.join(BASE, "models", "preprocessor.pkl")


def train():
    df = pd.read_csv(DATA_PATH)

    df.drop("customerID", axis=1, inplace=True)

    pre = Preprocessor()
    df = pre.fit_transform(df)

    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(pre, PREPROCESSOR_PATH)

    print("✅ Model trained successfully")


if __name__ == "__main__":
    train()