from forge.generators import (
    GeneratorFactory,
    ModuleGenerator,
    ServiceGenerator,
    PluginGenerator,
)


def test_plugin_generator_factory():

    generator = GeneratorFactory.create(
        "plugin"
    )

    assert isinstance(
        generator,
        PluginGenerator,
    )
