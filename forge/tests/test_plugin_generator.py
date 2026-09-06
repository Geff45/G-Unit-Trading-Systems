from forge.generators.plugin_generator import PluginGenerator


def test_plugin_generator_can_be_created(tmp_path):
    generator = PluginGenerator(tmp_path)

    assert generator is not None


def test_plugin_generator_has_generate_method(tmp_path):
    generator = PluginGenerator(tmp_path)

    assert hasattr(generator, "generate")
    assert callable(generator.generate)