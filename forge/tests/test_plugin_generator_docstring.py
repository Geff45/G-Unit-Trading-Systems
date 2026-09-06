import ast

from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_creates_module_docstring(
    tmp_path,
):
    generator = PluginGenerator(tmp_path)

    result = generator.generate("example_plugin")

    source = result.read_text(
        encoding="utf-8"
    )

    tree = ast.parse(source)

    assert ast.get_docstring(tree) == (
        "Generated Forge plugin: example_plugin."
    )