from gunit.modules.market_data_provider import MarketDataProvider
from gunit.modules.market_data_snapshot import MarketDataSnapshot


class SnapshotMarketDataProvider(MarketDataProvider):

    def get_latest_price(self, symbol: str):
        return 1.1234

    def get_latest_snapshot(self, symbol: str):
        return MarketDataSnapshot(
            symbol=symbol,
            price=1.1234,
            timestamp=1700000000.0,
        )


def test_market_data_provider_defines_latest_snapshot_boundary():
    assert hasattr(MarketDataProvider, "get_latest_snapshot")


def test_market_data_provider_can_return_market_data_snapshot():
    provider = SnapshotMarketDataProvider()

    snapshot = provider.get_latest_snapshot("EURUSD")

    assert isinstance(snapshot, MarketDataSnapshot)


def test_market_data_snapshot_preserves_required_fields():
    provider = SnapshotMarketDataProvider()

    snapshot = provider.get_latest_snapshot("EURUSD")

    assert snapshot.symbol == "EURUSD"
    assert snapshot.price == 1.1234
    assert snapshot.timestamp == 1700000000.0
