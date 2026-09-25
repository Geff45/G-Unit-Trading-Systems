import pytest

from gunit.modules.market_data_snapshot import MarketDataSnapshot


@pytest.mark.parametrize("symbol", [None, 123, 1.2345])
def test_market_data_snapshot_rejects_non_string_symbol(symbol):
    with pytest.raises(ValueError):
        MarketDataSnapshot(
            symbol=symbol,
            price=1.23456,
            timestamp=1700000000.0,
        )


@pytest.mark.parametrize("symbol", ["", " ", "   ", "\t", "\n"])
def test_market_data_snapshot_rejects_blank_symbol(symbol):
    with pytest.raises(ValueError):
        MarketDataSnapshot(
            symbol=symbol,
            price=1.23456,
            timestamp=1700000000.0,
        )


def test_market_data_snapshot_preserves_valid_symbol():
    symbol = "EURUSD"

    snapshot = MarketDataSnapshot(
        symbol=symbol,
        price=1.23456,
        timestamp=1700000000.0,
    )

    assert snapshot.symbol == symbol


def test_market_data_snapshot_does_not_normalize_symbol():
    symbol = "eurusd"

    snapshot = MarketDataSnapshot(
        symbol=symbol,
        price=1.23456,
        timestamp=1700000000.0,
    )

    assert snapshot.symbol == symbol