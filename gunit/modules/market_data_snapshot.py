from dataclasses import dataclass


@dataclass(frozen=True)
class MarketDataSnapshot:
    symbol: str
    price: float
    timestamp: float
