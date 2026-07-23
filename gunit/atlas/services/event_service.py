"""
Atlas event service.
"""

from __future__ import annotations

from gunit.core.events.bus import EventBus


class EventService:
    """
    Atlas wrapper around EventBus.
    """

    def __init__(self) -> None:
        self._bus = EventBus()

    @property
    def bus(self) -> EventBus:
        return self._bus