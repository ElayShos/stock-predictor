import yfinance as yf
import pandas as pd
from pathlib import Path


class StockDataCollector:

    def __init__(self, data_folder="data/raw"):
        self.data_folder = Path(data_folder)
        self.data_folder.mkdir(parents=True, exist_ok=True)

    def download(self, ticker, period="10y"):

        df = yf.download(ticker, period=period)

        # Fix multi-index columns if needed
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        file_path = self.data_folder / f"{ticker}.csv"
        df.to_csv(file_path)

        return df