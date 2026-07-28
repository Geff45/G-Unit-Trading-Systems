"""
Module context.
"""

from __future__ import annotations

from dataclasses import dataclass

from gunit.di.service_collection import ServiceCollection


@dataclass(slots=True)
class ModuleContext:
    """
    Context passed to modules.
    """

    services: ServiceCollection