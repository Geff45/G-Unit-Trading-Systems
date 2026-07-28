from gunit.configuration import Configuration


def test_configuration():
    config = Configuration()

    config.set("host", "localhost")

    assert config.get("host") == "localhost"
    assert config.contains("host")

    config.remove("host")

    assert not config.contains("host")
