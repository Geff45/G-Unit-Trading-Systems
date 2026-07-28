from gunit.pipeline.builder import PipelineBuilder
from gunit.pipeline.context import PipelineContext
from gunit.pipeline.pipeline import Pipeline
from gunit.pipeline.stage import PipelineStage


class DemoStage(PipelineStage):

    def execute(
        self,
        context: PipelineContext,
    ) -> None:

        context.set("builder", True)


def test_builder_returns_pipeline():

    builder = PipelineBuilder()

    builder.use(DemoStage())

    pipeline = builder.build()

    assert isinstance(pipeline, Pipeline)


def test_builder_pipeline_executes():

    builder = PipelineBuilder()

    builder.use(DemoStage())

    pipeline = builder.build()

    context = PipelineContext()

    pipeline.execute(context)

    assert context.get("builder")