import pytest

from gunit.modules.market_data_module import MarketDataService
from gunit.modules.market_data_snapshot import MarketDataSnapshot
from gunit.modules.market_data_provider import MarketDataProvider


class FailingMarketDataProvider(MarketDataProvider):

    def get_latest_price(self, symbol: str):
        raise RuntimeError("price provider failure")

    def get_latest_snapshot(self, symbol: str):
        raise ConnectionError("snapshot provider failure")


def test_market_data_service_propagates_price_provider_exception():
    service = MarketDataService(FailingMarketDataProvider())

    with pytest.raises(RuntimeError, match="price provider failure"):
        service.get_latest_price("EURUSD")


def test_market_data_service_preserves_price_provider_exception_type():
    service = MarketDataService(FailingMarketDataProvider())

    with pytest.raises(RuntimeError):
        service.get_latest_price("EURUSD")


def test_market_data_service_propagates_snapshot_provider_exception():
    service = MarketDataService(FailingMarketDataProvider())

    with pytest.raises(ConnectionError, match="snapshot provider failure"):
        service.get_latest_snapshot("EURUSD")


def test_market_data_service_preserves_snapshot_provider_exception_type():
    service = MarketDataService(FailingMarketDataProvider())

    with pytest.raises(ConnectionError):
        service.get_latest_snapshot("EURUSD")


def test_market_data_service_does_not_replace_provider_failure_with_snapshot():
    service = MarketDataService(FailingMarketDataProvider())

    with pytest.raises(ConnectionError):
        result = service.get_latest_snapshot("EURUSD")
        assert isinstance(result, MarketDataSnapshot)
