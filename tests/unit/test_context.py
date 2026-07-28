from gunit.middleware.context import MiddlewareContext


def test_context_store_value():

    ctx = MiddlewareContext()

    ctx.set("version", "1.0")

    assert ctx.get("version") == "1.0"


def test_context_contains():

    ctx = MiddlewareContext()

    ctx.set("name", "G-Unit")

    assert ctx.contains("name")


def test_context_remove():

    ctx = MiddlewareContext()

    ctx.set("x", 100)

    ctx.remove("x")

    assert not ctx.contains("x")


def test_context_clear():

    ctx = MiddlewareContext()

    ctx.set("a", 1)

    ctx.set("b", 2)

    ctx.clear()

    assert ctx.data == {}


def test_context_cancel():

    ctx = MiddlewareContext()

    assert not ctx.cancelled

    ctx.cancel()

    assert ctx.cancelled