import pytest

from gunit.modules.market_data_module import MarketDataService
from gunit.modules.market_data_provider import MarketDataProvider
from gunit.modules.market_data_snapshot import MarketDataSnapshot


class ResultMarketDataProvider(MarketDataProvider):
    def __init__(self) -> None:
        self.price = 1.23456
        self.snapshot = MarketDataSnapshot(
            symbol="EURUSD",
            price=1.23456,
            timestamp=1700000000.0,
        )

    def get_latest_price(self, symbol: str):
        return self.price

    def get_latest_snapshot(self, symbol: str):
        return self.snapshot


def test_market_data_service_returns_provider_price_unchanged():
    provider = ResultMarketDataProvider()
    service = MarketDataService(provider)

    result = service.get_latest_price("EURUSD")

    assert result is provider.price


def test_market_data_service_returns_provider_snapshot_unchanged():
    provider = ResultMarketDataProvider()
    service = MarketDataService(provider)

    result = service.get_latest_snapshot("EURUSD")

    assert result is provider.snapshot


def test_market_data_service_preserves_snapshot_values():
    provider = ResultMarketDataProvider()
    service = MarketDataService(provider)

    result = service.get_latest_snapshot("EURUSD")

    assert result.symbol == "EURUSD"
    assert result.price == 1.23456
    assert result.timestamp == 1700000000.0
