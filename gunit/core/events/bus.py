"""
Event Bus
"""

from __future__ import annotations

from collections import defaultdict

from .dispatcher import EventDispatcher
from .event import Event
from .exceptions import DuplicateSubscription
from .handler import EventHandler


class EventBus:
    """
    Central event bus.
    """

    def __init__(self) -> None:
        self._dispatcher = EventDispatcher()
        self._subscriptions: dict[type, list[EventHandler]] = (
            defaultdict(list)
        )

    def subscribe(
        self,
        event_type: type,
        handler: EventHandler,
    ) -> None:

        handlers = self._subscriptions[event_type]

        if handler in handlers:
            raise DuplicateSubscription()

        handlers.append(handler)

    def unsubscribe(
        self,
        event_type: type,
        handler: EventHandler,
    ) -> None:

        handlers = self._subscriptions[event_type]

        if handler in handlers:
            handlers.remove(handler)

    def publish(
        self,
        event: Event,
    ) -> None:

        for handler in self._subscriptions[type(event)]:
            self._dispatcher.dispatch(
                handler,
                event,
            )