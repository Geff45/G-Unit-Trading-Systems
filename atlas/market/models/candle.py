from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass(slots=True)
class Candle:

    instrument: str

    timeframe: str

    timestamp: datetime

    open: float

    high: float

    low: float

    close: float

    volume: float