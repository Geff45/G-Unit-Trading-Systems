from gunit.modules import ModuleBuilder
from gunit.modules import Module
from gunit.modules import ModuleContext


class DummyModule(Module):
    @property
    def name(self):
        return "Module"

    def configure(self, context: ModuleContext):
        pass


def test_builder():
    builder = ModuleBuilder()

    builder.add(DummyModule())

    registry = builder.build()

    assert len(registry.modules) == 1