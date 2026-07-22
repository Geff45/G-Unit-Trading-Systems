import pytest

from gunit.core.config.exceptions import ConfigurationValidationError
from gunit.core.config.validator import ConfigurationValidator


def test_missing_required_section():

    validator = ConfigurationValidator()

    with pytest.raises(ConfigurationValidationError):
        validator.validate({})