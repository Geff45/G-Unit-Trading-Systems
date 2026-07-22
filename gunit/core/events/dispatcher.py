"""
Event dispatcher.
"""

from __future__ import annotations

from .event import Event
from .exceptions import HandlerFailed
from .handler import EventHandler


class EventDispatcher:
    """
    Executes event handlers.
    """

    def dispatch(
        self,
        handler: EventHandler,
        event: Event,
    ) -> None:
        try:
            handler.handle(event)
        except Exception as exc:
            raise HandlerFailed(str(exc)) from exc