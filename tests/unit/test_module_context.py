from gunit.di.service_collection import ServiceCollection
from gunit.modules import ModuleContext


def test_context():
    services = ServiceCollection()

    context = ModuleContext(services)

    assert context.services is services