import yfinance as yf
import pandas as pd

from src.sp500 import SP500Loader
from src.indicators import IndicatorCalculator
from src.feature_engineering import FeatureEngineer
from src.model import StockModel


def main():

    print("\n--------------------------------")
    print("S&P500 Prediction Model")
    print("--------------------------------\n")

    tickers = SP500Loader().load()

    print("Downloading market data...")

    data = yf.download(
        tickers,
        period="5y",
        group_by="ticker",
        threads=True
    )

    indicators = IndicatorCalculator()

    while True:

        months = int(input("\nEnter prediction horizon in months: "))
        weeks_forward = months * 4

        feature_engineer = FeatureEngineer(weeks_forward)

        all_X = []
        all_y = []

        print("\nProcessing stocks...\n")

        for i, ticker in enumerate(tickers):

            try:

                print(f"{i+1}/{len(tickers)} Processing {ticker}")

                df = data[ticker].copy()

                df = indicators.add_indicators(df)

                df = feature_engineer.create_target(df)

                X, y = feature_engineer.prepare(df)

                all_X.append(X)
                all_y.append(y)

            except Exception as e:

                print("Skipping", ticker, e)

        print("\nCombining datasets...")

        X = pd.concat(all_X)
        y = pd.concat(all_y)

        print("Total samples:", len(X))

        model = StockModel()

        print("\nTraining model...")

        model.train(X, y)

        latest_features = X.iloc[-1:]

        prediction = model.predict(latest_features)[0]

        print("\n--------------------------------")
        print("Market Forecast")
        print("--------------------------------")

        print(f"Prediction horizon: {months} months")
        print("Expected return:", round(prediction * 100, 2), "%")

        if prediction > 0:
            print("Expected direction: UP")
        else:
            print("Expected direction: DOWN")

        again = input("\nCheck another timeframe? (y/n): ").lower()

        if again != "y":
            print("\nExiting program.")
            break


if __name__ == "__main__":
    main()