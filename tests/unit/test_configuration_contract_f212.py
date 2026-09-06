from pathlib import Path

import json

from gunit.configuration import (
    Configuration,
    ConfigurationBuilder,
    ConfigurationManager,
    ConfigurationProvider,
    ConfigurationRoot,
    ConfigurationSection,
    ConfigurationSource,
    EnvironmentProvider,
    JsonProvider,
    MemoryProvider,
)


class MemorySourceStub(ConfigurationSource):

    def __init__(self, values):
        self.values = values

    def build(self):
        provider = MemoryProvider()

        for key, value in self.values.items():
            provider.add(key, value)

        return provider


def test_all_configuration_components_are_public():
    assert Configuration is not None
    assert ConfigurationBuilder is not None
    assert ConfigurationManager is not None
    assert ConfigurationProvider is not None
    assert ConfigurationRoot is not None
    assert ConfigurationSection is not None
    assert ConfigurationSource is not None


def test_configuration_supports_complete_basic_lifecycle():
    config = Configuration()

    config.set("host", "localhost")
    config.set("port", 8080)

    assert config.get("host") == "localhost"
    assert config.get("missing", "default") == "default"
    assert config.contains("host")

    assert dict(config.items()) == {
        "host": "localhost",
        "port": 8080,
    }

    config.remove("host")

    assert not config.contains("host")

    config.clear()

    assert dict(config.items()) == {}


def test_configuration_builder_is_fluent():
    builder = ConfigurationBuilder()

    assert builder.add("name", "Atlas") is builder
    assert builder.add("version", "1.0") is builder

    config = builder.build()

    assert config.get("name") == "Atlas"
    assert config.get("version") == "1.0"


def test_configuration_manager_is_configuration_compatible():
    manager = ConfigurationManager()

    manager.set("environment", "development")

    assert manager.get("environment") == "development"
    assert manager.contains("environment")


def test_configuration_provider_has_load_and_save_contract():
    provider = ConfigurationProvider()

    assert provider.load() == {}
    assert hasattr(provider, "save")
    assert callable(provider.save)


def test_memory_provider_round_trip():
    provider = MemoryProvider()

    provider.add("host", "localhost")
    provider.add("port", 8080)

    values = provider.load()

    assert values["host"] == "localhost"
    assert values["port"] == 8080


def test_configuration_source_build_contract():
    source = ConfigurationSource()

    try:
        source.build()
    except NotImplementedError:
        pass
    else:
        raise AssertionError(
            "Base ConfigurationSource.build() must remain abstract by contract"
        )


def test_configuration_root_is_configuration_compatible():
    root = ConfigurationRoot()

    root.set("language", "python")

    assert root.get("language") == "python"
    assert root.contains("language")


def test_configuration_section_represents_key_and_value():
    section = ConfigurationSection(
        "database",
        {"host": "localhost"},
    )

    assert section.key == "database"
    assert section.value == {"host": "localhost"}


def test_environment_provider_is_a_configuration_provider():
    provider = EnvironmentProvider()

    assert isinstance(provider, ConfigurationProvider)

    values = provider.load()

    assert isinstance(values, dict)


def test_json_provider_loads_json_file(tmp_path):
    config_file = Path(tmp_path) / "config.json"

    config_file.write_text(
        json.dumps(
            {
                "application": {
                    "name": "Atlas",
                },
                "debug": True,
            }
        ),
        encoding="utf-8",
    )

    provider = JsonProvider()

    values = provider.load_file(config_file)

    assert values["application"]["name"] == "Atlas"
    assert values["debug"] is True


def test_configuration_source_builds_a_provider():
    source = MemorySourceStub(
        {
            "environment": "development",
            "debug": True,
        }
    )

    provider = source.build()

    assert isinstance(provider, ConfigurationProvider)
    assert provider.load() == {
        "environment": "development",
        "debug": True,
    }


def test_configuration_builder_accepts_sources():
    source = MemorySourceStub(
        {
            "application": "Atlas",
            "version": "1.0",
        }
    )

    config = (
        ConfigurationBuilder()
        .add_source(source)
        .build()
    )

    assert config.get("application") == "Atlas"
    assert config.get("version") == "1.0"


def test_configuration_root_aggregates_provider_values():
    provider = MemoryProvider()

    provider.add("host", "localhost")
    provider.add("port", 8080)

    root = ConfigurationRoot(
        providers=[provider]
    )

    assert root.get("host") == "localhost"
    assert root.get("port") == 8080


def test_configuration_manager_can_manage_a_root():
    provider = MemoryProvider()
    provider.add("environment", "production")

    root = ConfigurationRoot(
        providers=[provider]
    )

    manager = ConfigurationManager(root)

    assert manager.get("environment") == "production"


def test_configuration_root_preserves_direct_configuration_values():
    root = ConfigurationRoot()

    root.set("local", "value")

    assert root.get("local") == "value"
