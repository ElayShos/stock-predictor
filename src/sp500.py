import pandas as pd
import requests


class SP500Loader:

    def load(self):

        url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        tables = pd.read_html(response.text)

        df = tables[0]

        tickers = df["Symbol"].tolist()

        # Yahoo uses BRK-B instead of BRK.B
        tickers = [t.replace(".", "-") for t in tickers]

        return tickers