from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from .event import Event


class EventHandler(ABC):

    @abstractmethod
    def handle(self, event: Event) -> None:
        """
        Process an event.
        """