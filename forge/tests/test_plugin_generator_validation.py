import pytest

from forge.generators.plugin_generator import PluginGenerator


@pytest.mark.parametrize(
    "name",
    [
        "",
        "123plugin",
        "plugin name",
        "plugin-name",
    ],
)
def test_plugin_generator_rejects_invalid_name(tmp_path, name):
    generator = PluginGenerator(tmp_path)

    with pytest.raises(ValueError):
        generator.generate(name)


def test_plugin_generator_accepts_valid_name(tmp_path):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("example_plugin")

    assert result == tmp_path / "plugins" / "example_plugin.py"