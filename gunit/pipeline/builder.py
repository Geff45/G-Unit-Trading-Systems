"""
Pipeline builder.
"""

from __future__ import annotations

from .pipeline import Pipeline
from .stage import PipelineStage


class PipelineBuilder:

    def __init__(self) -> None:
        self._pipeline = Pipeline()

    def use(
        self,
        stage: PipelineStage,
    ) -> "PipelineBuilder":

        self._pipeline.add(stage)

        return self

    def build(self) -> Pipeline:

        return self._pipeline