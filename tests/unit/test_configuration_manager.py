from gunit.configuration import ConfigurationManager


def test_configuration_manager():
    manager = ConfigurationManager()

    manager.set("theme", "dark")

    assert manager.get("theme") == "dark"
