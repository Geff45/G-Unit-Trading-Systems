import pytest

from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_preserves_source_after_duplicate_attempt(
    tmp_path,
):
    generator = PluginGenerator(tmp_path)

    first = generator.generate("example_plugin")

    original_content = first.read_text(
        encoding="utf-8"
    )

    with pytest.raises(FileExistsError):
        generator.generate("example_plugin")

    assert first.read_text(
        encoding="utf-8"
    ) == original_content
