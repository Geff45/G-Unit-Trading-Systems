from gunit.middleware.context import MiddlewareContext
from gunit.middleware.middleware import Middleware


class DummyMiddleware(Middleware):

    def __init__(self):

        self.executed = False

    def invoke(self, context, next_delegate):

        self.executed = True

        next_delegate(context)


def test_middleware_invocation():

    middleware = DummyMiddleware()

    called = False

    def next_delegate(ctx: MiddlewareContext):

        nonlocal called

        called = True

    middleware.invoke(
        MiddlewareContext(),
        next_delegate,
    )

    assert middleware.executed

    assert called