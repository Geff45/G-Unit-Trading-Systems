from pathlib import Path

from forge.generators import (
    BaseGenerator,
    ModuleGenerator,
    ServiceGenerator,
    PluginGenerator,
)


def test_module_generator_inherits_base_generator():
    assert issubclass(
        ModuleGenerator,
        BaseGenerator,
    )


def test_service_generator_inherits_base_generator():
    assert issubclass(
        ServiceGenerator,
        BaseGenerator,
    )


def test_plugin_generator_inherits_base_generator():
    assert issubclass(
        PluginGenerator,
        BaseGenerator,
    )


def test_all_generators_expose_project_root(tmp_path):
    generators = [
        ModuleGenerator(tmp_path),
        ServiceGenerator(tmp_path),
        PluginGenerator(tmp_path),
    ]

    for generator in generators:
        assert hasattr(generator, "project_root")
        assert Path(generator.project_root) == tmp_path.resolve()


def test_all_generators_expose_write_file(tmp_path):
    generators = [
        ModuleGenerator(tmp_path),
        ServiceGenerator(tmp_path),
        PluginGenerator(tmp_path),
    ]

    for generator in generators:
        assert callable(generator.write_file)


def test_base_generator_generate_is_defined():
    assert callable(BaseGenerator.generate)


def test_plugin_generator_uses_common_file_writer(tmp_path):
    generator = PluginGenerator(tmp_path)

    result = generator.generate(
        "example_plugin"
    )

    expected = (
        tmp_path
        / "plugins"
        / "example_plugin.py"
    )

    assert result == expected
    assert expected.exists()


def test_generators_share_same_base_class():
    assert (
        ModuleGenerator.__mro__[1]
        is BaseGenerator
    )

    assert (
        ServiceGenerator.__mro__[1]
        is BaseGenerator
    )

    assert (
        PluginGenerator.__mro__[1]
        is BaseGenerator
    )
