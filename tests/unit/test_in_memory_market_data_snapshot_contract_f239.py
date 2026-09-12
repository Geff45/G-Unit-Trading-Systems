import pytest

from gunit.modules.in_memory_market_data_provider import (
    InMemoryMarketDataProvider,
)
from gunit.modules.market_data_snapshot import MarketDataSnapshot


def test_in_memory_provider_returns_latest_snapshot():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})

    snapshot = provider.get_latest_snapshot("EURUSD")

    assert isinstance(snapshot, MarketDataSnapshot)


def test_in_memory_provider_snapshot_preserves_symbol_and_price():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})

    snapshot = provider.get_latest_snapshot("EURUSD")

    assert snapshot.symbol == "EURUSD"
    assert snapshot.price == 1.1234


def test_in_memory_provider_snapshot_rejects_blank_symbol():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})

    with pytest.raises(ValueError):
        provider.get_latest_snapshot("   ")


def test_in_memory_provider_snapshot_rejects_unknown_symbol():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})

    with pytest.raises(KeyError):
        provider.get_latest_snapshot("GBPUSD")
