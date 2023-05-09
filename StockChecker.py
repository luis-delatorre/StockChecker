import os
import argparse
import requests
from dotenv import load_dotenv
from urllib.parse import urljoin


load_dotenv()
API_HOST = os.environ['API_HOST']
API_KEY = os.environ['API_KEY']
CONTENT = "application/octet-stream"


class StockChecker:

    def __init__(self, sym):
        self.symbol = sym
        self.url = "https://realstonks.p.rapidapi.com/"
        self.headers = {
            "content-type": CONTENT,
            "X-RapidAPI-Host": API_HOST,
            "X-RapidAPI-Key": API_KEY
        }

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, sym):
        self.symbol = sym

    def get_url(self):
        url = urljoin(self.url, self.get_symbol())
        return url

    def get_headers(self):
        return self.headers

    def set_headers(self, cont, host, key):
        self.headers = {
            "content-type": cont,
            "X-RapidAPI-Host": host,
            "X-RapidAPI-Key": key
        }

    def get_stock_info(self):
        response = requests.get(self.get_url(), headers=self.get_headers())
        return response

    def print_stock_info(self):
        resp_json = self.get_stock_info().json()
        print("{}: {}".format(self.get_symbol(), resp_json))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Sends requests to a Finance Rest API to get stock information on the specified ticker.'
    )
    parser.add_argument('symbol', metavar='Symbol', type=str, help='Name of stock symbol.')
    args = parser.parse_args()

    stk = StockChecker(sym=args.symbol)
    print("Checking data for {}.".format(args.symbol))
    stk.print_stock_info()

    while True:
        symbol_input = input("Enter symbol [or press ENTER to quit]: ")
        if symbol_input == "":
            break
        else:
            print("Checking data for {}.".format(symbol_input))

            stk.set_symbol(symbol_input)
            stk.print_stock_info()
