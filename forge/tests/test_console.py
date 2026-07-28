from forge.console import Console


def test_console():

    Console.write("Hello")

    Console.info("Info")

    Console.success("Success")

    Console.warning("Warning")

    Console.error("Error")