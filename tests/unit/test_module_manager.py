from gunit.di.service_collection import ServiceCollection
from gunit.modules import Module
from gunit.modules import ModuleContext
from gunit.modules import ModuleManager


class DummyModule(Module):
    def __init__(self):
        self.started = False
        self.stopped = False

    @property
    def name(self):
        return "Dummy"

    def configure(self, context: ModuleContext):
        pass

    def start(self, context: ModuleContext):
        self.started = True

    def stop(self, context: ModuleContext):
        self.stopped = True


def test_manager():
    manager = ModuleManager()

    module = DummyModule()

    manager.add(module)

    context = ModuleContext(ServiceCollection())

    manager.start(context)

    assert module.started

    manager.stop(context)

    assert module.stopped