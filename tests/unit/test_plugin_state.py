from gunit.plugins import PluginState


def test_plugin_state():
    assert PluginState.CREATED.value == "created"
    assert PluginState.LOADED.value == "loaded"
    assert PluginState.INITIALIZED.value == "initialized"
    assert PluginState.STARTED.value == "started"
    assert PluginState.STOPPED.value == "stopped"
    assert PluginState.FAILED.value == "failed"
