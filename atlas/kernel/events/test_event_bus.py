from kernel.events.event import Event
from kernel.events.event_bus import EventBus
from kernel.events.subscriber import EventSubscriber


class LoggerSubscriber(EventSubscriber):

    def handle(self, event):

        print(
            f"[LOGGER] {event.event_type} "
            f"from {event.source}"
        )


class DecisionSubscriber(EventSubscriber):

    def handle(self, event):

        print(
            f"[DECISION] received "
            f"{event.event_type}"
        )


bus = EventBus()

bus.subscribe("trend.changed", LoggerSubscriber())
bus.subscribe("trend.changed", DecisionSubscriber())

bus.publish(
    Event(
        event_type="trend.changed",
        source="trend_engine",
        payload={
            "direction": "BUY",
            "confidence": 0.91
        }
    )
)