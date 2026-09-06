from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_creates_plugins_init_file(tmp_path):
    generator = PluginGenerator(tmp_path)

    generator.generate("example_plugin")

    init_file = tmp_path / "plugins" / "__init__.py"

    assert init_file.exists()
    assert init_file.is_file()


def test_plugin_generator_init_file_is_valid_python(tmp_path):
    generator = PluginGenerator(tmp_path)

    generator.generate("example_plugin")

    init_file = tmp_path / "plugins" / "__init__.py"

    source = init_file.read_text(encoding="utf-8")

    compile(source, str(init_file), "exec")