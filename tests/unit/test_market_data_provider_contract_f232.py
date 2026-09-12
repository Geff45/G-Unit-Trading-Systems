import inspect

import pytest

from gunit.modules.market_data_provider import MarketDataProvider


def test_market_data_provider_is_abstract():
    assert inspect.isabstract(MarketDataProvider)


def test_market_data_provider_defines_latest_price_boundary():
    assert hasattr(MarketDataProvider, "get_latest_price")


def test_market_data_provider_requires_symbol_argument():
    signature = inspect.signature(MarketDataProvider.get_latest_price)

    assert list(signature.parameters) == ["self", "symbol"]


def test_market_data_provider_cannot_be_instantiated():
    with pytest.raises(TypeError):
        MarketDataProvider()
