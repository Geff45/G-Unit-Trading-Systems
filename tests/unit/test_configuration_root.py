from gunit.configuration import ConfigurationRoot


def test_configuration_root():
    root = ConfigurationRoot()

    root.set("language", "python")

    assert root.get("language") == "python"
