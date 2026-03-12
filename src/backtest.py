import pandas as pd


def backtest(df: pd.DataFrame, model, features):

    df = df.copy()

    df["Prediction"] = model.predict(df[features])

    df["Market_Return"] = df["Close"].pct_change()

    df["Strategy_Return"] = df["Market_Return"] * df["Prediction"]

    df = df.dropna()

    df["Market_Cumulative"] = (1 + df["Market_Return"]).cumprod()
    df["Strategy_Cumulative"] = (1 + df["Strategy_Return"]).cumprod()

    strategy_return = df["Strategy_Cumulative"].iloc[-1]
    market_return = df["Market_Cumulative"].iloc[-1]

    print("Strategy return:", round(strategy_return, 2))
    print("Market return:", round(market_return, 2))

    return df