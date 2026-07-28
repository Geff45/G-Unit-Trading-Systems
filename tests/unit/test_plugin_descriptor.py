from gunit.plugins import PluginDescriptor


def test_plugin_descriptor():
    descriptor = PluginDescriptor(
        name="Example",
        version="1.0.0",
        author="G-Unit",
        description="Example plugin"
    )

    assert descriptor.name == "Example"
    assert descriptor.version == "1.0.0"
    assert descriptor.author == "G-Unit"
    assert descriptor.description == "Example plugin"
