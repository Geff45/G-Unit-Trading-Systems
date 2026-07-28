from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class CommandContext:
    """
    Runtime information passed to every command.
    """

    args: List[str] = field(default_factory=list)

    options: Dict[str, str] = field(default_factory=dict)

    working_directory: str = "."