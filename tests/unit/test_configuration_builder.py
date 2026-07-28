from gunit.configuration import ConfigurationBuilder


def test_configuration_builder():
    config = (
        ConfigurationBuilder()
        .add("name", "Atlas")
        .add("version", "1.0")
        .build()
    )

    assert config.get("name") == "Atlas"
    assert config.get("version") == "1.0"
