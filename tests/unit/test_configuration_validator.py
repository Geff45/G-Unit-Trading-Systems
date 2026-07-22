from gunit.core.config.validator import ConfigurationValidator


def test_configuration_validator_accepts_valid_configuration():

    validator = ConfigurationValidator()

    config = validator.validate(
        {
            "system": {
                "name": "G-UNIT",
                "version": "0.1.0",
                "mode": "development",
            },
            "logging": {
                "level": "INFO",
                "file": "logs/gunit.log",
            },
            "workspace": {
                "root": "workspace",
            },
            "kernel": {
                "auto_boot": True,
            },
            "security": {
                "telemetry": True,
            },
        }
    )

    assert config.system.name == "G-UNIT"
    assert config.kernel.auto_boot is True