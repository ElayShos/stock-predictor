import yfinance as yf
import pandas as pd
from pathlib import Path


DATA_PATH = Path("data/raw")


def download_stock(ticker: str, period="5y", interval="1d"):

    DATA_PATH.mkdir(parents=True, exist_ok=True)

    data = yf.download(ticker, period=period, interval=interval)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    file_path = DATA_PATH / f"{ticker}.csv"
    data.to_csv(file_path)

    return data
