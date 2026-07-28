from gunit.scheduler.schedule import Schedule


def test_schedule():

    schedule = Schedule(
        interval=5.0,
        repeat=True,
    )

    assert schedule.interval == 5.0
    assert schedule.repeat