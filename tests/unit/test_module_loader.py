from gunit.modules import Module
from gunit.modules import ModuleContext
from gunit.modules import ModuleLoader


class DummyModule(Module):
    @property
    def name(self):
        return "Dummy"

    def configure(self, context: ModuleContext):
        pass


def test_loader():
    loader = ModuleLoader()

    module = DummyModule()

    loaded = loader.load(module)

    assert loaded is module