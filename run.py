from src.data_collector import download_stock
from src.indicators import compute_indicators
from src.feature_engineering import prepare_features
from src.model import train_model


def main():

    df = download_stock("AAPL")

    df = compute_indicators(df)

    X, y = prepare_features(df)

    model = train_model(X, y)


if __name__ == "__main__":
    main()