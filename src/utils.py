class TickerLoader:

    def __init__(self, file_path="tickers.txt"):
        self.file_path = file_path

    def load(self):
        tickers = []

        with open(self.file_path, "r") as f:
            for line in f:
                ticker = line.strip()
                if ticker:
                    tickers.append(ticker)

        return tickers