from gunit.di.service_collection import ServiceCollection
from gunit.modules import Module, ModuleContext


class TestModule(Module):
    @property
    def name(self) -> str:
        return "Test"

    def configure(self, context: ModuleContext) -> None:
        pass


def test_module_defaults():
    module = TestModule()

    assert module.name == "Test"
    assert module.version == "1.0.0"


def test_module_lifecycle():
    context = ModuleContext(ServiceCollection())

    module = TestModule()

    module.configure(context)
    module.start(context)
    module.stop(context)