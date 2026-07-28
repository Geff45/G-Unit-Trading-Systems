from gunit.di import ServiceCollection
from gunit.extensions import (
    Extension,
    ExtensionContext,
    ExtensionDescriptor,
)


class DemoExtension(Extension):

    def configure(self, context):
        self.context = context

    def initialize(self):
        self.initialized = True

    def enable(self):
        self.enabled = True

    def disable(self):
        self.disabled = True


def test_extension():

    services = ServiceCollection()

    context = ExtensionContext(services)

    descriptor = ExtensionDescriptor(
        name="Demo",
        version="1.0.0",
        author="G-Unit",
        description="Demo Extension",
    )

    extension = DemoExtension()

    extension.descriptor = descriptor

    extension.configure(context)
    extension.initialize()
    extension.enable()
    extension.disable()

    assert extension.context is context
    assert extension.initialized
    assert extension.enabled
    assert extension.disabled
