import pandas as pd


def create_target(df: pd.DataFrame):

    # predict if tomorrow goes up
    df["Tomorrow"] = df["Close"].shift(-1)

    df["Target"] = (df["Tomorrow"] > df["Close"]).astype(int)

    return df


def prepare_features(df: pd.DataFrame):

    df = create_target(df)

    features = [
        "Close",
        "Volume",
        "SMA_20",
        "SMA_50",
        "RSI"
    ]

    df = df.dropna()

    X = df[features]
    y = df["Target"]

    return X, y