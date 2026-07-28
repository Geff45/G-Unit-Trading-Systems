from gunit.extensions import ExtensionContext
from gunit.di import ServiceCollection


def test_extension_context():

    services = ServiceCollection()

    context = ExtensionContext(services)

    assert context.services is services
