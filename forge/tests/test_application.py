from forge.application import ForgeApplication


def test_register_command():

    app = ForgeApplication()

    def hello():
        return "Hello"

    app.register("hello", hello)

    assert app.has_command("hello")


def test_execute_command():

    app = ForgeApplication()

    def add(a, b):
        return a + b

    app.register("add", add)

    assert app.execute("add", 2, 3) == 5


def test_command_names():

    app = ForgeApplication()

    app.register("b", lambda: None)
    app.register("a", lambda: None)

    assert app.command_names() == ["a", "b"]