from gunit.di.service_collection import ServiceCollection
from gunit.modules import Module
from gunit.modules.module_context import ModuleContext
from gunit.modules.module_registry import ModuleRegistry


class DummyModule(Module):
    @property
    def name(self):
        return "Dummy"

    def configure(self, context: ModuleContext):
        pass


def test_registry():
    registry = ModuleRegistry()

    module = DummyModule()

    registry.register(module)

    assert len(registry.modules) == 1