from gunit.modules.market_data_provider import MarketDataProvider


class InMemoryMarketDataProvider(MarketDataProvider):
    """
    Deterministic market-data provider for development and testing.
    """

    def __init__(self, prices: dict[str, float]) -> None:
        self._prices = dict(prices)

    def get_latest_price(self, symbol: str):
        if not symbol or not symbol.strip():
            raise ValueError("symbol must not be empty")

        if symbol not in self._prices:
            raise KeyError(f"No price configured for symbol: {symbol}")

        return self._prices[symbol]
