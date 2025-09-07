# bingx_analyzer.py

import requests

class BingXAnalyzer:
    def __init__(self):
        self.base_url = "https://api.bingx.com/api/v1/"

    def get_open_interest(self, symbol):
        response = requests.get(f"{self.base_url}open_interest?symbol={symbol}")
        return response.json()

    def get_volume(self, symbol):
        response = requests.get(f"{self.base_url}volume?symbol={symbol}")
        return response.json()

    def analyze(self, symbols):
        for symbol in symbols:
            open_interest = self.get_open_interest(symbol)
            volume = self.get_volume(symbol)
            print(f"Open Interest for {symbol}: {open_interest}")
            print(f"Volume for {symbol}: {volume}")

if __name__ == "__main__":
    analyzer = BingXAnalyzer()
    analyzer.analyze(['BTC', 'ETH'])