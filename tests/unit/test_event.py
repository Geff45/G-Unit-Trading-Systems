from gunit.core.events import Event


class TestEvent(Event):
    pass


def test_event_creation():

    event = TestEvent("kernel")

    assert event.source == "kernel"
    assert event.name == "TestEvent"
    assert event.event_id