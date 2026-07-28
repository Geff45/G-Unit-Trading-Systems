from gunit.configuration import MemoryProvider


def test_memory_provider():
    provider = MemoryProvider()

    provider.add("mode", "debug")

    assert provider.load()["mode"] == "debug"
