import pytest
from StockChecker import StockChecker


@pytest.fixture
def req():
    return StockChecker('IAS')


def test_successful_call(req):
    req.get_stock_info()
    assert req.get_response().status_code == 200


def test_expected_fields_are_present(req):
    req.get_stock_info()
    fields = ['price', 'change_point', 'change_percentage', 'total_vol']
    for i in fields:
        assert i in req.get_response().json()


def test_call_fails_with_no_symbol(req):
    req.set_symbol('')
    req.get_stock_info()
    assert req.get_response().status_code == 404


def test_call_fails_bad_api_key(req):
    req.set_headers(api_key="abc123")
    req.get_stock_info()
    assert req.get_response().status_code == 403
