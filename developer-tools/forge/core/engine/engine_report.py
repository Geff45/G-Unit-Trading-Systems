"""
Atlas Forge Engine Report

Version: 1.0.0
"""

from dataclasses import dataclass


@dataclass(slots=True)
class EngineReport:

    state: str
    version: str

    registered_services: int

    running_services: int

    failed_services: int