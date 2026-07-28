import pytest

from gunit.configuration import ConfigurationSource


def test_configuration_source():
    source = ConfigurationSource()

    with pytest.raises(NotImplementedError):
        source.build()
