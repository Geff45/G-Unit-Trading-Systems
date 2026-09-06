import pytest

from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_rejects_existing_plugin(tmp_path):
    generator = PluginGenerator(tmp_path)

    plugin_file = tmp_path / "plugins" / "example_plugin.py"
    plugin_file.parent.mkdir(parents=True)
    plugin_file.write_text(
        "existing content\n",
        encoding="utf-8",
    )

    with pytest.raises(FileExistsError):
        generator.generate("example_plugin")


def test_plugin_generator_preserves_existing_plugin(tmp_path):
    generator = PluginGenerator(tmp_path)

    plugin_file = tmp_path / "plugins" / "example_plugin.py"
    plugin_file.parent.mkdir(parents=True)
    original_content = "existing content\n"

    plugin_file.write_text(
        original_content,
        encoding="utf-8",
    )

    with pytest.raises(FileExistsError):
        generator.generate("example_plugin")

    assert plugin_file.read_text(
        encoding="utf-8"
    ) == original_content