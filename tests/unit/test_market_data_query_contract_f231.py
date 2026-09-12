import pytest

from gunit.modules.market_data_module import (
    MarketDataService,
    UnavailableMarketDataProvider,
)


def test_market_data_query_accepts_symbol_as_string():
    service = MarketDataService(UnavailableMarketDataProvider())

    with pytest.raises(NotImplementedError):
        service.get_latest_price("EURUSD")


@pytest.mark.parametrize("symbol", ["", " ", "   ", "\t", "\n"])
def test_market_data_query_rejects_blank_symbol(symbol):
    service = MarketDataService(UnavailableMarketDataProvider())

    with pytest.raises(ValueError):
        service.get_latest_price(symbol)


def test_market_data_query_does_not_normalize_symbol_before_boundary():
    service = MarketDataService(UnavailableMarketDataProvider())

    with pytest.raises(NotImplementedError):
        service.get_latest_price("eurusd")


def test_market_data_query_does_not_fabricate_price_result():
    service = MarketDataService(UnavailableMarketDataProvider())

    with pytest.raises(NotImplementedError):
        service.get_latest_price("EURUSD")
