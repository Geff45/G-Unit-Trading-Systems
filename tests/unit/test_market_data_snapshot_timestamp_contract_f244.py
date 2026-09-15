import pytest

from gunit.modules.market_data_snapshot import MarketDataSnapshot


def test_market_data_snapshot_preserves_integer_timestamp():
    snapshot = MarketDataSnapshot(
        symbol="EURUSD",
        price=1.23456,
        timestamp=1700000000,
    )

    assert snapshot.timestamp == 1700000000


def test_market_data_snapshot_preserves_float_timestamp():
    snapshot = MarketDataSnapshot(
        symbol="EURUSD",
        price=1.23456,
        timestamp=1700000000.123456,
    )

    assert snapshot.timestamp == 1700000000.123456


def test_market_data_snapshot_rejects_boolean_timestamp():
    with pytest.raises(TypeError):
        MarketDataSnapshot(
            symbol="EURUSD",
            price=1.23456,
            timestamp=True,
        )


def test_market_data_snapshot_preserves_timestamp_without_normalization():
    timestamp = 1700000000.123456

    snapshot = MarketDataSnapshot(
        symbol="EURUSD",
        price=1.23456,
        timestamp=timestamp,
    )

    assert snapshot.timestamp is timestamp
