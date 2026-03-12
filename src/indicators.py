import pandas as pd


def add_moving_averages(df: pd.DataFrame):

    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()

    return df


def add_rsi(df: pd.DataFrame, window=14):

    delta = df["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))

    return df


def compute_indicators(df: pd.DataFrame):

    df = add_moving_averages(df)
    df = add_rsi(df)

    return df