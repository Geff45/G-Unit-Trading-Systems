from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_keeps_name_consistent(
    tmp_path,
):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("market_plugin")

    assert result.name == "market_plugin.py"

    source = result.read_text(
        encoding="utf-8"
    )

    assert "market_plugin" in source
