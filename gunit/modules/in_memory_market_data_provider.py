import time

from gunit.modules.market_data_provider import MarketDataProvider
from gunit.modules.market_data_snapshot import MarketDataSnapshot


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

    def get_latest_snapshot(self, symbol: str) -> MarketDataSnapshot:
        if not symbol or not symbol.strip():
            raise ValueError("symbol must not be empty")

        if symbol not in self._prices:
            raise KeyError(f"No price configured for symbol: {symbol}")

        return MarketDataSnapshot(
            symbol=symbol,
            price=self._prices[symbol],
            timestamp=time.time(),
        )
