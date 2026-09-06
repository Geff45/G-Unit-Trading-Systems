from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_writes_utf8_source(
    tmp_path,
):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("unicode_plugin")

    content = result.read_text(
        encoding="utf-8"
    )

    assert content.startswith(
        '"""Generated Forge plugin: unicode_plugin."""'
    )
