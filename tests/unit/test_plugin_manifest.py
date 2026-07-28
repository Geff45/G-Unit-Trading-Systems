from gunit.plugins import PluginManifest


def test_plugin_manifest():
    manifest = PluginManifest(
        name="Example",
        version="1.0.0",
        author="G-Unit",
        description="Example plugin",
        dependencies=["core", "scheduler"]
    )

    assert manifest.name == "Example"
    assert manifest.version == "1.0.0"
    assert manifest.dependencies == ["core", "scheduler"]
