from gunit.pipeline.context import PipelineContext
from gunit.pipeline.stage import PipelineStage


class DummyStage(PipelineStage):

    def execute(
        self,
        context: PipelineContext,
    ) -> None:

        context.set("executed", True)


def test_stage_executes():

    context = PipelineContext()

    stage = DummyStage()

    stage.execute(context)

    assert context.get("executed") is True