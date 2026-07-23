"""
G-UNIT Update Phase 00

Initial bootstrap phase for the Forge update system.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


PHASE_NAME = "phase00"
PHASE_VERSION = "0.1.0"


def run(update: Any) -> bool:
    """
    Execute the bootstrap update phase.

    Parameters
    ----------
    update:
        Update context supplied by Forge.

    Returns
    -------
    bool
        True when the phase completes successfully.
    """

    if hasattr(update, "logger"):
        update.logger.info("Running %s...", PHASE_NAME)

    root = getattr(update, "root", Path.cwd())

    if hasattr(update, "workspace"):
        workspace = update.workspace
    else:
        workspace = root

    if hasattr(update, "logger"):
        update.logger.info("Workspace: %s", workspace)

    if hasattr(update, "metadata"):
        update.metadata["phase"] = PHASE_NAME
        update.metadata["version"] = PHASE_VERSION

    return True