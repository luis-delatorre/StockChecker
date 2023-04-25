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
        self.response = None

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

    def get_response(self):
        return self.response

    def set_response(self, resp):
        self.response = resp

    def get_stock_info(self):
        response = requests.get(self.get_url(), headers=self.get_headers())
        self.set_response(response)

    def print_stock_info(self):
        resp_json = self.get_response().json()
        print("{}: {}".format(self.get_symbol(), resp_json))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Sends requests to a Finance Rest API to get stock information on the specified ticker.'
    )
    parser.add_argument('symbol', metavar='s', type=str, help='Name of stock symbol.')
    args = parser.parse_args()
    ticker = args.symbol

    a = StockChecker(sym=ticker)
    a.get_stock_info()
    a.print_stock_info()

    a.set_symbol('TSLA')
    a.get_stock_info()
    a.print_stock_info()

    print('api_key: {}'.format(a.api_key))
    print('api_host: {}'.format(a.api_host))
