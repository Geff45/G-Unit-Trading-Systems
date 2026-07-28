"""
Pipeline result.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class PipelineResult:
    success: bool
    executed: int