"""
Atlas Forge Context Paths

Defines the project directory structure.

Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ContextPaths:
    """
    Stores all important Atlas Forge paths.
    """

    project_root: Path

    forge_root: Path

    templates: Path

    logs: Path

    cache: Path

    database: Path

    workspace: Path

    config: Path

    python_backend: Path

    mt4_project: Path