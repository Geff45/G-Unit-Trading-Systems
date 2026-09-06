from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_documentation_ends_with_newline(
    tmp_path,
):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("example_plugin")

    source = result.read_text(
        encoding="utf-8"
    )

    assert source.endswith("\n")