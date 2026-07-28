from gunit.commands.command_builder import (
    CommandBuilder,
)
from gunit.commands.command_bus import (
    CommandBus,
)


def test_builder():

    builder = CommandBuilder()

    bus = builder.build()

    assert isinstance(
        bus,
        CommandBus,
    )