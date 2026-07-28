from gunit.plugins import Plugin, PluginContext
from gunit.di import ServiceCollection


class SamplePlugin(Plugin):
    def __init__(self):
        self.started = False
        self.stopped = False
        self.context = None

    def configure(self, context: PluginContext) -> None:
        self.context = context

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        self.stopped = True


def test_plugin_lifecycle():
    services = ServiceCollection()
    context = PluginContext(services)

    plugin = SamplePlugin()

    plugin.configure(context)
    plugin.start()
    plugin.stop()

    assert plugin.context is context
    assert plugin.started
    assert plugin.stopped
