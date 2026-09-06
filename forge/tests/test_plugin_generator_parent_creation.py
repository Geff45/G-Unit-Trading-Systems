from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_creates_missing_project_root(tmp_path):
    project_root = (
        tmp_path
        / "new_project"
        / "nested"
    )

    generator = PluginGenerator(project_root)

    result = generator.generate("example_plugin")

    assert project_root.exists()
    assert project_root.is_dir()

    assert result == (
        project_root
        / "plugins"
        / "example_plugin.py"
    )

    assert result.exists()
    assert result.is_file()
