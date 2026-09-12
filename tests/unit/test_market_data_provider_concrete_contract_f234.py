from gunit.modules.market_data_provider import MarketDataProvider


class TestMarketDataProvider(MarketDataProvider):

    def get_latest_price(self, symbol: str):
        return 123.45


def test_concrete_market_data_provider_can_be_implemented():
    provider = TestMarketDataProvider()

    assert provider.get_latest_price("EURUSD") == 123.45


def test_concrete_market_data_provider_preserves_symbol():
    received = []

    class RecordingMarketDataProvider(MarketDataProvider):

        def get_latest_price(self, symbol: str):
            received.append(symbol)
            return 123.45

    provider = RecordingMarketDataProvider()

    provider.get_latest_price("EURUSD")

    assert received == ["EURUSD"]
