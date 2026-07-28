from forge.commands.make import execute


def test_make(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    execute(
        "module",
        "TradeEngine",
    )