from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class SettingsModel:
    workspace: Path = Path.cwd()
    log_level: str = "INFO"
    debug: bool = False
    version: str = "0.1.0"
    data: dict = field(default_factory=dict)