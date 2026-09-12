from gunit.modules.in_memory_market_data_provider import (
    InMemoryMarketDataProvider,
)
from gunit.modules.market_data_module import MarketDataService
from gunit.modules.market_data_snapshot import MarketDataSnapshot


def test_market_data_service_exposes_latest_snapshot():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})
    service = MarketDataService(provider)

    snapshot = service.get_latest_snapshot("EURUSD")

    assert isinstance(snapshot, MarketDataSnapshot)


def test_market_data_service_snapshot_preserves_provider_data():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})
    service = MarketDataService(provider)

    snapshot = service.get_latest_snapshot("EURUSD")

    assert snapshot.symbol == "EURUSD"
    assert snapshot.price == 1.1234
