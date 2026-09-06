from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_does_not_modify_existing_plugin(
    tmp_path,
):
    generator = PluginGenerator(tmp_path)

    first = generator.generate("first_plugin")
    original_content = first.read_text(
        encoding="utf-8"
    )

    generator.generate("second_plugin")

    assert first.read_text(
        encoding="utf-8"
    ) == original_content
