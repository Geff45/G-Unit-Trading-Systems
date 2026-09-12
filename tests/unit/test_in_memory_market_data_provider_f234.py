import pytest

from gunit.modules.in_memory_market_data_provider import (
    InMemoryMarketDataProvider,
)
from gunit.modules.market_data_provider import MarketDataProvider


def test_in_memory_provider_implements_market_data_provider():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})

    assert isinstance(provider, MarketDataProvider)


def test_in_memory_provider_returns_configured_price():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})

    assert provider.get_latest_price("EURUSD") == 1.1234


def test_in_memory_provider_rejects_blank_symbol():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})

    with pytest.raises(ValueError):
        provider.get_latest_price("   ")


def test_in_memory_provider_rejects_unknown_symbol():
    provider = InMemoryMarketDataProvider({"EURUSD": 1.1234})

    with pytest.raises(KeyError):
        provider.get_latest_price("GBPUSD")
