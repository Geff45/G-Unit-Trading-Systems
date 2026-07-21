from dataclasses import dataclass
from datetime import timedelta
from typing import Callable


@dataclass(slots=True)
class ScheduledTask:

    name: str

    interval: timedelta

    callback: Callable

    enabled: bool = True