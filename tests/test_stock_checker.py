import os
import pytest
from dotenv import load_dotenv
from StockChecker import StockChecker


load_dotenv()
API_KEY = os.environ['API_KEY']
API_HOST = os.environ['API_HOST']
CONTENT = "application/octet-stream"


@pytest.fixture
def obj():
    return StockChecker('IAS')


def test_successful_call(obj):
    assert obj.get_stock_info().status_code == 200


def test_expected_response_fields_are_present(obj):
    fields = ['price', 'change_point', 'change_percentage', 'total_vol']
    for i in fields:
        assert i in obj.get_stock_info().json()


def test_call_fails_with_no_symbol(obj):
    obj.set_symbol('')
    assert obj.get_stock_info().status_code == 404


def test_call_fails_with_bad_api_key(obj):
    obj.set_headers(cont=CONTENT, key='abc123', host=API_HOST)
    assert obj.get_stock_info().status_code == 403
