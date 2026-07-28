from forge.framework import CommandResult


def test_result():

    result = CommandResult.ok(
        "done"
    )

    assert result.success
    assert result.message == "done"


def test_failed_result():

    result = CommandResult.fail(
        "failed"
    )

    assert result.success is False
    assert result.message == "failed"
