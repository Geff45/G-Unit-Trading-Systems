"""
Module descriptor.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ModuleDescriptor:
    """
    Describes a module.
    """

    name: str
    version: str