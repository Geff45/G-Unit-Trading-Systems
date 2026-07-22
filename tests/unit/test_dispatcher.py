from gunit.core.events import Event
from gunit.core.events import EventDispatcher
from gunit.core.events import EventHandler


class TestEvent(Event):
    pass


class TestHandler(EventHandler):

    def __init__(self):

        self.called = False

    def handle(self, event):

        self.called = True


def test_dispatch():

    dispatcher = EventDispatcher()

    handler = TestHandler()

    dispatcher.dispatch(
        handler,
        TestEvent("kernel"),
    )

    assert handler.called