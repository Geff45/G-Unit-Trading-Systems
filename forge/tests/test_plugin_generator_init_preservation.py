from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_preserves_existing_init_file(tmp_path):
    generator = PluginGenerator(tmp_path)

    init_file = tmp_path / "plugins" / "__init__.py"
    init_file.parent.mkdir(parents=True)

    original_content = (
        '"""Existing plugin package."""\n'
    )

    init_file.write_text(
        original_content,
        encoding="utf-8",
    )

    generator.generate("example_plugin")

    assert init_file.read_text(
        encoding="utf-8"
    ) == original_content


def test_plugin_generator_still_creates_plugin_when_init_exists(tmp_path):
    generator = PluginGenerator(tmp_path)

    init_file = tmp_path / "plugins" / "__init__.py"
    init_file.parent.mkdir(parents=True)
    init_file.write_text(
        '"""Existing plugin package."""\n',
        encoding="utf-8",
    )

    result = generator.generate("example_plugin")

    assert result.exists()
    assert result.is_file()