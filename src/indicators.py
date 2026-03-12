import pandas as pd


class IndicatorCalculator:

    def add_indicators(self, df: pd.DataFrame):

        df = df.resample("W").last()

        df["SMA_10"] = df["Close"].rolling(10).mean()
        df["SMA_30"] = df["Close"].rolling(30).mean()

        delta = df["Close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()

        rs = avg_gain / avg_loss

        df["RSI"] = 100 - (100 / (1 + rs))

        df["Return_1M"] = df["Close"].pct_change(4)
        df["Return_3M"] = df["Close"].pct_change(12)
        df["Return_6M"] = df["Close"].pct_change(26)

        return df