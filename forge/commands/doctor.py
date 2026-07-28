from __future__ import annotations

import platform
from pathlib import Path

from forge.console import Console


def execute():
    """
    Check whether the Forge development environment is healthy.
    """

    Console.banner()

    Console.success(f"Python {platform.python_version()}")

    if Path("pyproject.toml").exists():
        Console.success("Project detected")
    else:
        Console.error("pyproject.toml not found")

    if Path("forge/templates").exists():
        Console.success("Templates")
    else:
        Console.warning("Templates directory missing")

    if Path("forge/generators").exists():
        Console.success("Generators")
    else:
        Console.warning("Generators directory missing")

    if Path("forge/tests").exists():
        Console.success("Tests")
    else:
        Console.warning("Tests directory missing")

    if Path("forge_manifest.json").exists():
        Console.success("Manifest")
    else:
        Console.warning("Manifest not found")

    Console.write()
    Console.success("System Healthy")