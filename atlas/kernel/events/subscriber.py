from abc import ABC, abstractmethod
from kernel.events.event import Event


class EventSubscriber(ABC):

    @abstractmethod
    def handle(self, event: Event):
        """Handle an event."""
        raise NotImplementedError