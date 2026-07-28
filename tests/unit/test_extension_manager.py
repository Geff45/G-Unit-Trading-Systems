from gunit.extensions import (
    Extension,
    ExtensionManager,
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


def test_manager():

    manager = ExtensionManager()

    extension = DemoExtension()

    extension.descriptor = ExtensionDescriptor(
        name="Demo",
        version="1.0.0",
        author="G-Unit",
        description="Demo",
    )

    manager.register(extension)

    assert manager.get("Demo") is extension

    manager.enable("Demo")
    assert extension.enabled

    manager.disable("Demo")
    assert extension.disabled
