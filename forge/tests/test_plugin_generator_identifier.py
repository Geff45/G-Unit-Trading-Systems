from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_accepts_python_identifier(tmp_path):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("TradeEngine")

    assert result == tmp_path / "plugins" / "TradeEngine.py"
    assert result.exists()
    assert result.is_file()
