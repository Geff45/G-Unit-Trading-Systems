from gunit.core.events import Event
from gunit.core.events import EventBus
from gunit.core.events import EventHandler


class BootEvent(Event):
    pass


class BootHandler(EventHandler):

    def __init__(self):

        self.called = False

    def handle(self, event):

        self.called = True


def test_event_bus_publish():

    bus = EventBus()

    handler = BootHandler()

    bus.subscribe(
        BootEvent,
        handler,
    )

    bus.publish(
        BootEvent("kernel"),
    )

    assert handler.called