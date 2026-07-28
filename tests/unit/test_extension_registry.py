from gunit.extensions import (
    Extension,
    ExtensionRegistry,
    ExtensionDescriptor,
)


class DemoExtension(Extension):

    def configure(self, context):
        pass

    def initialize(self):
        pass

    def enable(self):
        self.enabled = True

    def disable(self):
        self.disabled = True


def make_extension(name):

    extension = DemoExtension()

    extension.descriptor = ExtensionDescriptor(
        name=name,
        version="1.0.0",
        author="G-Unit",
        description="Demo",
    )

    return extension


def test_registry():

    registry = ExtensionRegistry()

    registry.register(make_extension("A"))
    registry.register(make_extension("B"))

    assert registry.get("A").descriptor.name == "A"
    assert registry.get("B").descriptor.name == "B"

    registry.unregister("A")

    assert registry.get("A") is None
    assert registry.get("B") is not None

    registry.clear()

    assert len(registry.all()) == 0
