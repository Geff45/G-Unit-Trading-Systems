from datetime import datetime, UTC

from market.models.tick import Tick
from market.models.candle import Candle

tick = Tick(
    instrument="EURUSD",
    timestamp=datetime.now(UTC),
    bid=1.17240,
    ask=1.17242,
    volume=10,
    spread=0.2
)

print(tick)

candle = Candle(
    instrument="EURUSD",
    timeframe="M15",
    timestamp=datetime.now(UTC),
    open=1.1700,
    high=1.1730,
    low=1.1690,
    close=1.1725,
    volume=1200
)

print(candle)