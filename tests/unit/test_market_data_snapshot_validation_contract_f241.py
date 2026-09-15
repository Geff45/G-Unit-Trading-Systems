import pytest

from gunit.modules.market_data_snapshot import MarketDataSnapshot


def test_market_data_snapshot_rejects_empty_symbol():
    with pytest.raises(ValueError):
        MarketDataSnapshot(
            symbol="",
            price=1.1234,
            timestamp=1700000000.0,
        )


def test_market_data_snapshot_rejects_blank_symbol():
    with pytest.raises(ValueError):
        MarketDataSnapshot(
            symbol="   ",
            price=1.1234,
            timestamp=1700000000.0,
        )


@pytest.mark.parametrize("price", ["1.1234", None])
def test_market_data_snapshot_rejects_non_numeric_price(price):
    with pytest.raises((TypeError, ValueError)):
        MarketDataSnapshot(
            symbol="EURUSD",
            price=price,
            timestamp=1700000000.0,
        )


@pytest.mark.parametrize("timestamp", ["1700000000", None])
def test_market_data_snapshot_rejects_non_numeric_timestamp(timestamp):
    with pytest.raises((TypeError, ValueError)):
        MarketDataSnapshot(
            symbol="EURUSD",
            price=1.1234,
            timestamp=timestamp,
        )


def test_market_data_snapshot_preserves_valid_values():
    snapshot = MarketDataSnapshot(
        symbol="EURUSD",
        price=1.1234,
        timestamp=1700000000.0,
    )

    assert snapshot.symbol == "EURUSD"
    assert snapshot.price == 1.1234
    assert snapshot.timestamp == 1700000000.0
