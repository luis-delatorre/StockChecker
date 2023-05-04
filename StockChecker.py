import os
import argparse
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ['API_KEY']
API_HOST = os.environ['API_HOST']
CONTENT = "application/octet-stream"


class StockChecker:

    def __init__(self, sym):
        self.symbol = sym
        self.url = "https://realstonks.p.rapidapi.com/"
        self.headers = {
            "content-type": CONTENT,
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, sym):
        self.symbol = sym

    def get_url(self):
        return self.url + self.get_symbol()

    def get_headers(self):
        return self.headers

    def set_headers(self, cont, key, host):
        self.headers = {
            "content-type": cont,
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": host
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
    stk.print_stock_info()

    while True:
        symbol_input = input("Enter symbol [or press ENTER to quit]: ")
        if symbol_input == "":
            break
        else:
            print("Checking data for {}.".format(symbol_input))

            stk.set_symbol(symbol_input)
            stk.print_stock_info()
