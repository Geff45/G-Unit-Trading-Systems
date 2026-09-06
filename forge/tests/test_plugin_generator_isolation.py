from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_writes_inside_project_root(tmp_path):
    project_root = tmp_path / "sample_project"

    generator = PluginGenerator(project_root)

    result = generator.generate("example_plugin")

    expected = (
        project_root
        / "plugins"
        / "example_plugin.py"
    )

    assert result == expected
    assert expected.exists()
    assert expected.is_file()
