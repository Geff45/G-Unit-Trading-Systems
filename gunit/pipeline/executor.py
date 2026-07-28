"""
Pipeline executor.
"""

from __future__ import annotations

from .context import PipelineContext
from .pipeline import Pipeline
from .result import PipelineResult


class PipelineExecutor:

    def execute(
        self,
        pipeline: Pipeline,
        context: PipelineContext,
    ) -> PipelineResult:

        return pipeline.execute(context)