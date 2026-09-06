from pathlib import Path

from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_returns_path_object(tmp_path):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("example_plugin")

    assert isinstance(result, Path)
    assert result == (
        tmp_path
        / "plugins"
        / "example_plugin.py"
    )
