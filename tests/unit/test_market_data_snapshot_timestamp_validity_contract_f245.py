import math

import pytest

from gunit.modules.market_data_snapshot import MarketDataSnapshot


@pytest.mark.parametrize("timestamp", [math.nan, math.inf, -math.inf])
def test_market_data_snapshot_rejects_non_finite_timestamp(timestamp):
    with pytest.raises(ValueError):
        MarketDataSnapshot(
            symbol="EURUSD",
            price=1.23456,
            timestamp=timestamp,
        )


def test_market_data_snapshot_preserves_finite_timestamp():
    timestamp = 1700000000.123456

    snapshot = MarketDataSnapshot(
        symbol="EURUSD",
        price=1.23456,
        timestamp=timestamp,
    )

    assert snapshot.timestamp == timestamp