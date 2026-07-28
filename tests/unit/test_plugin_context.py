from gunit.plugins import PluginContext
from gunit.di import ServiceCollection


def test_plugin_context():
    services = ServiceCollection()
    context = PluginContext(services)

    assert context.services is services
