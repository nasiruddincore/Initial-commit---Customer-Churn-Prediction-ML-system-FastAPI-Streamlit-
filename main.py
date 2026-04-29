import argparse
import pandas as pd
import joblib
from src.predict import predict
from src.utils import explain

MODEL_PATH = "models/churn_model.pkl"


def train():
    from src.train import model  # ensures training runs
    print("Training completed and model saved.")


def run_prediction():
    print("Running sample prediction...")

    sample_data = {
        "tenure": 5,
        "MonthlyCharges": 80.5,
        "TotalCharges": 400.0,
        "Contract": 1,
        "InternetService": 2
    }

    result = predict(sample_data)
    print("Prediction (1=Churn, 0=No Churn):", result)


def evaluate():
    print("Evaluating model...")

    df = pd.read_csv("data/churn.csv")
    df.dropna(inplace=True)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    model = joblib.load(MODEL_PATH)
    preds = model.predict(X)

    from sklearn.metrics import accuracy_score
    print("Accuracy:", accuracy_score(y, preds))


def run_explain():
    print("Generating SHAP explainability...")
    explain()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--train", action="store_true", help="Train model")
    parser.add_argument("--predict", action="store_true", help="Run prediction")
    parser.add_argument("--evaluate", action="store_true", help="Evaluate model")
    parser.add_argument("--explain", action="store_true", help="Run SHAP")

    args = parser.parse_args()

    if args.train:
        train()

    elif args.predict:
        run_prediction()

    elif args.evaluate:
        evaluate()

    elif args.explain:
        run_explain()

    else:
        print("Please provide a command:")
        print("--train | --predict | --evaluate | --explain")