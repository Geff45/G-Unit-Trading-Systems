from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_creates_independent_plugins(tmp_path):
    generator = PluginGenerator(tmp_path)

    first = generator.generate("first_plugin")
    second = generator.generate("second_plugin")

    assert first.exists()
    assert second.exists()

    assert first != second

    assert first.read_text(encoding="utf-8") != ""
    assert second.read_text(encoding="utf-8") != ""
