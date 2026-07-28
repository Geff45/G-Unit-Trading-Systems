from gunit.pipeline.context import PipelineContext
from gunit.pipeline.pipeline import Pipeline
from gunit.pipeline.stage import PipelineStage


class FirstStage(PipelineStage):

    def execute(
        self,
        context: PipelineContext,
    ) -> None:

        context.set("first", True)


class SecondStage(PipelineStage):

    def execute(
        self,
        context: PipelineContext,
    ) -> None:

        context.set("second", True)


def test_pipeline_executes_all():

    pipeline = Pipeline()

    pipeline.add(FirstStage())

    pipeline.add(SecondStage())

    context = PipelineContext()

    result = pipeline.execute(context)

    assert result.success

    assert result.executed == 2

    assert context.get("first")

    assert context.get("second")


def test_empty_pipeline():

    pipeline = Pipeline()

    result = pipeline.execute(PipelineContext())

    assert result.executed == 0