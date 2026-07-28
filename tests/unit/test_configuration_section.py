from gunit.configuration import ConfigurationSection


def test_configuration_section():
    section = ConfigurationSection("database", "sqlite")

    assert section.key == "database"
    assert section.value == "sqlite"
