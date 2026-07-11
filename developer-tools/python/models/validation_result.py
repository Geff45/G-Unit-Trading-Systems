"""
=========================================================
ATLAS Forge

Validation Result Model

Feature:
    DTF-003
=========================================================
"""

from dataclasses import dataclass


@dataclass
class ValidationResult:

    name: str

    status: str

    message: str