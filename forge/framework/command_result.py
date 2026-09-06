from dataclasses import dataclass


@dataclass
class CommandResult:

    success: bool
    message: str
    data: object = None


    @classmethod
    def ok(cls, message, data=None):

        return cls(
            True,
            message,
            data
        )


    @classmethod
    def success_result(cls, message, data=None):

        return cls.ok(
            message,
            data
        )


    @classmethod
    def fail(cls, message):

        return cls(
            False,
            message,
            None
        )
