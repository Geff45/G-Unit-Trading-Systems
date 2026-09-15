import math

import pytest

from gunit.modules.market_data_snapshot import MarketDataSnapshot


@pytest.mark.parametrize("price", [math.nan, math.inf, -math.inf])
def test_market_data_snapshot_rejects_non_finite_price(price):
    with pytest.raises(ValueError):
        MarketDataSnapshot(
            symbol="EURUSD",
            price=price,
            timestamp=1700000000.0,
        )


def test_market_data_snapshot_preserves_finite_integer_price():
    price = 123

    snapshot = MarketDataSnapshot(
        symbol="EURUSD",
        price=price,
        timestamp=1700000000.0,
    )

    assert snapshot.price == price


def test_market_data_snapshot_preserves_finite_float_price():
    price = 1.23456789

    snapshot = MarketDataSnapshot(
        symbol="EURUSD",
        price=price,
        timestamp=1700000000.0,
    )

    assert snapshot.price == price