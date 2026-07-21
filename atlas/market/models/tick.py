from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass(slots=True)
class Tick:

    instrument: str

    timestamp: datetime

    bid: float

    ask: float

    volume: float

    spread: float