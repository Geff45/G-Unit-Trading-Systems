from gunit.scheduler.schedule import Schedule
from gunit.scheduler.scheduled_job import ScheduledJob


def action():
    pass


def test_job():

    job = ScheduledJob(
        name="Heartbeat",
        action=action,
        schedule=Schedule(1.0),
    )

    assert job.name == "Heartbeat"
    assert job.enabled