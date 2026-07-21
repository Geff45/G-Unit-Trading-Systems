"""
Enterprise Version Model
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Version:
    """Semantic version."""

    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"