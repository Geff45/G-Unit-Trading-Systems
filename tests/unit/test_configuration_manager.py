from pathlib import Path

import yaml

from gunit.core.config import ConfigurationManager


def test_configuration_manager_loads_configuration(tmp_path):
    config_file = tmp_path / "default.yaml"

    config_data = {
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

    config_file.write_text(
        yaml.safe_dump(config_data),
        encoding="utf-8",
    )

    manager = ConfigurationManager()

    config = manager.load(config_file)

    assert manager.loaded
    assert config.system.name == "G-UNIT"
    assert config.kernel.auto_boot is True