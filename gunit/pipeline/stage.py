"""
Pipeline stage.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .context import PipelineContext


class PipelineStage(ABC):
    """
    Base pipeline stage.
    """

    @abstractmethod
    def execute(
        self,
        context: PipelineContext,
    ) -> None:
        ...