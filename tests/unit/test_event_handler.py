from gunit.core.events import Event
from gunit.core.events import EventHandler


class TestEvent(Event):
    pass


class TestHandler(EventHandler):

    def __init__(self):
        self.called = False

    def handle(self, event):

        self.called = True


def test_handler_receives_event():

    handler = TestHandler()

    handler.handle(TestEvent("kernel"))

    assert handler.called