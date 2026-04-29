import pandas as pd
from sklearn.preprocessing import LabelEncoder

class Preprocessor:
    def __init__(self):
        self.encoders = {}
        self.columns = None

    def fit_transform(self, df: pd.DataFrame):
        df = df.copy()

        # Drop missing
        df.dropna(inplace=True)

        # Store column order
        self.columns = df.columns.tolist()

        # Encode categorical columns
        for col in df.select_dtypes(include='object').columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            self.encoders[col] = le

        return df

    def transform(self, df: pd.DataFrame):
        df = df.copy()

        # Apply saved encoders
        for col, le in self.encoders.items():
            if col in df.columns:
                df[col] = le.transform(df[col])

        # Ensure column order consistency
        df = df.reindex(columns=self.columns, fill_value=0)

        return df