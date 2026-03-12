import yfinance as yf


class AnalystDataCollector:

    def get(self, ticker):

        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "analyst_target": info.get("targetMeanPrice"),
            "analyst_count": info.get("numberOfAnalystOpinions"),
            "recommendation": info.get("recommendationMean")
        }