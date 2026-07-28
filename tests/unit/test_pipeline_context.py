from gunit.pipeline.context import PipelineContext


def test_context_set_and_get():

    context = PipelineContext()

    context.set("name", "Atlas")

    assert context.get("name") == "Atlas"


def test_context_default_value():

    context = PipelineContext()

    assert context.get("missing") is None

    assert context.get("missing", 42) == 42


def test_context_overwrite():

    context = PipelineContext()

    context.set("x", 1)

    context.set("x", 2)

    assert context.get("x") == 2