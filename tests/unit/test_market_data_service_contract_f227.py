import pytest

from gunit.modules.market_data_module import (
    MarketDataService,
    UnavailableMarketDataProvider,
)


def test_market_data_service_has_identity():
    service = MarketDataService(UnavailableMarketDataProvider())

    assert service.name == "MarketDataService"
    assert service.version == "1.0.0"


def test_market_data_service_defines_latest_price_boundary():
    service = MarketDataService(UnavailableMarketDataProvider())

    assert hasattr(service, "get_latest_price")


def test_market_data_service_latest_price_requires_symbol():
    service = MarketDataService(UnavailableMarketDataProvider())

    with pytest.raises(NotImplementedError):
        service.get_latest_price("EURUSD")


@pytest.mark.parametrize("symbol", ["", "   "])
def test_market_data_service_rejects_empty_symbol(symbol):
    service = MarketDataService(UnavailableMarketDataProvider())

    with pytest.raises(ValueError):
        service.get_latest_price(symbol)
