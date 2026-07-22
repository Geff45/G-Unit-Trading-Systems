from dataclasses import dataclass

from .handler import EventHandler


@dataclass(slots=True)
class Subscription:
    event_type: type
    handler: EventHandler