"""
Atlas Forge Generation Report

Version: 1.0.0
"""

from dataclasses import dataclass


@dataclass(slots=True)
class GenerationReport:

    directories_created: int = 0
    directories_existing: int = 0

    files_created: int = 0
    files_existing: int = 0

    templates_applied: int = 0

    errors: int = 0

    @property
    def success(self) -> bool:
        return self.errors == 0