"""
=========================================================
ATLAS Forge

Base Validation Check

Feature:
    DTF-003

Author:
    GUTS Development Team
=========================================================
"""

from abc import ABC, abstractmethod


class BaseCheck(ABC):
    """
    Base class for all validation checks.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self):
        """
        Execute the validation check.
        Must return a dictionary.
        """
        pass