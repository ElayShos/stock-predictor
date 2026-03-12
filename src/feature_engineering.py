import pandas as pd


class FeatureEngineer:

    def __init__(self, weeks_forward):
        self.weeks_forward = weeks_forward

    def create_target(self, df):

        future_price = df["Close"].shift(-self.weeks_forward)

        df["Future_Return"] = (future_price / df["Close"]) - 1

        return df

    def prepare(self, df):

        features = [
            "Close",
            "Volume",
            "SMA_10",
            "SMA_30",
            "RSI",
            "Return_1M",
            "Return_3M",
            "Return_6M"
        ]

        df = df.dropna()

        X = df[features]
        y = df["Future_Return"]

        return X, y