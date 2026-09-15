from dataclasses import dataclass


@dataclass(frozen=True)
class MarketDataSnapshot:
    symbol: str
    price: float
    timestamp: float

    def __post_init__(self) -> None:
        if not isinstance(self.symbol, str) or not self.symbol.strip():
            raise ValueError("symbol must not be empty")

        if not isinstance(self.price, (int, float)):
            raise TypeError("price must be numeric")

        if isinstance(self.timestamp, bool) or not isinstance(
            self.timestamp, (int, float)
        ):
            raise TypeError("timestamp must be numeric")