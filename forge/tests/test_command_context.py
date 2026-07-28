from forge.framework import CommandContext


def test_context():

    context = CommandContext(
        args=["version"]
    )

    assert context.args == ["version"]
