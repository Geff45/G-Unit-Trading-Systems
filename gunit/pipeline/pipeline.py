"""
Pipeline.
"""

from __future__ import annotations

from .context import PipelineContext
from .result import PipelineResult
from .stage import PipelineStage


class Pipeline:
    """
    Execution pipeline.
    """

    def __init__(self) -> None:
        self._stages: list[PipelineStage] = []

    def add(
        self,
        stage: PipelineStage,
    ) -> "Pipeline":
        self._stages.append(stage)
        return self

    def execute(
        self,
        context: PipelineContext,
    ) -> PipelineResult:

        for stage in self._stages:
            stage.execute(context)

        return PipelineResult(
            success=True,
            executed=len(self._stages),
        )