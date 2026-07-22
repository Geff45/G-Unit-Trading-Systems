from gunit.core.services import Service
from gunit.core.services import ServiceRegistry


class DummyService(Service):

    def __init__(self):
        self._running = False

    @property
    def name(self):
        return "dummy"

    def start(self):
        self._running = True

    def stop(self):
        self._running = False

    @property
    def running(self):
        return self._running


def test_registry_register():

    registry = ServiceRegistry()

    service = DummyService()

    registry.register(service)

    assert registry.exists("dummy")

    assert registry.get("dummy") is service


def test_registry_unregister():

    registry = ServiceRegistry()

    service = DummyService()

    registry.register(service)

    registry.unregister("dummy")

    assert not registry.exists("dummy")


def test_registry_clear():

    registry = ServiceRegistry()

    registry.register(DummyService())

    registry.clear()

    assert len(registry) == 0