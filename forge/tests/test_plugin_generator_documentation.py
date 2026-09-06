from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_includes_plugin_name_in_documentation(tmp_path):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("market_plugin")

    source = result.read_text(encoding="utf-8")

    assert '"""Generated Forge plugin: market_plugin."""' in source
