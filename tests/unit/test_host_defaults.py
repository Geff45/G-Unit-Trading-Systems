from gunit.host.defaults import HostDefaults


def test_default_environment():

    options = HostDefaults.create()

    assert options.environment == "Development"


def test_development_environment():

    options = HostDefaults.development()

    assert options.environment == "Development"


def test_production_environment():

    options = HostDefaults.production()

    assert options.environment == "Production"