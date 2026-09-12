import inspect

from gunit.modules.market_data_snapshot import MarketDataSnapshot


def test_market_data_snapshot_is_constructible():
    snapshot = MarketDataSnapshot(
        symbol="EURUSD",
        price=1.1234,
        timestamp=1700000000.0,
    )

    assert snapshot.symbol == "EURUSD"
    assert snapshot.price == 1.1234
    assert snapshot.timestamp == 1700000000.0


def test_market_data_snapshot_exposes_required_fields():
    signature = inspect.signature(MarketDataSnapshot)

    assert list(signature.parameters) == [
        "symbol",
        "price",
        "timestamp",
    ]


def test_market_data_snapshot_is_immutable():
    snapshot = MarketDataSnapshot(
        symbol="EURUSD",
        price=1.1234,
        timestamp=1700000000.0,
    )

    try:
        snapshot.price = 1.2000
    except (AttributeError, TypeError):
        pass
    else:
        raise AssertionError("MarketDataSnapshot must be immutable")
