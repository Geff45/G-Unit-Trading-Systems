from gunit.scheduler.job_context import JobContext


def test_context():

    context = JobContext()

    assert context.metadata == {}
    assert not context.cancelled