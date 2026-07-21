from collections import defaultdict

from kernel.events.event import Event
from kernel.events.subscriber import EventSubscriber


class EventBus:

    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(
        self,
        event_type: str,
        subscriber: EventSubscriber,
    ):

        self._subscribers[event_type].append(subscriber)

    def publish(self, event: Event):

        for subscriber in self._subscribers.get(event.event_type, []):
            subscriber.handle(event)