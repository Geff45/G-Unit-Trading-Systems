from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_creates_plugin_file(tmp_path):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("example_plugin")

    plugin_file = tmp_path / "plugins" / "example_plugin.py"

    assert plugin_file.exists()
    assert plugin_file.is_file()
    assert result == plugin_file


def test_plugin_generator_creates_plugins_directory(tmp_path):
    generator = PluginGenerator(tmp_path)

    generator.generate("example_plugin")

    plugins_directory = tmp_path / "plugins"

    assert plugins_directory.exists()
    assert plugins_directory.is_dir()