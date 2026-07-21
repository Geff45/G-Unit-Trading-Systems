from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass(slots=True)
class MarketSnapshot:

    instrument: str

    timeframe: str

    timestamp: datetime

    open: float

    high: float

    low: float

    close: float

    bid: float

    ask: float

    volume: float

    spread: float

    volatility: float

    session: str