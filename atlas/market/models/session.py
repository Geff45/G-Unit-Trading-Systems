from dataclasses import dataclass
from datetime import time


@dataclass(slots=True)
class TradingSession:

    name: str

    start: time

    end: time

    timezone: str