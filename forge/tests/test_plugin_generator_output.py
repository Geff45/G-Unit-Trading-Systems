from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_creates_python_module(tmp_path):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("example_plugin")

    assert result.read_text(encoding="utf-8") == (
        '"""Generated Forge plugin: example_plugin."""\n'
    )


def test_plugin_generator_output_is_valid_python(tmp_path):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("example_plugin")

    source = result.read_text(encoding="utf-8")

    compile(source, str(result), "exec")