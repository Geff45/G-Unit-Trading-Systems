from gunit.pipeline.context import PipelineContext
from gunit.pipeline.executor import PipelineExecutor
from gunit.pipeline.pipeline import Pipeline
from gunit.pipeline.stage import PipelineStage


class ExecutionStage(PipelineStage):

    def execute(
        self,
        context: PipelineContext,
    ) -> None:

        context.set("done", True)


def test_executor_runs_pipeline():

    pipeline = Pipeline()

    pipeline.add(ExecutionStage())

    executor = PipelineExecutor()

    context = PipelineContext()

    result = executor.execute(
        pipeline,
        context,
    )

    assert result.success

    assert result.executed == 1

    assert context.get("done")