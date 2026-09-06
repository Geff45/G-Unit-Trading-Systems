from forge.commands.make import execute


def test_make(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    result = execute(
        "module",
        "TradeEngine",
    )

    assert result.success is True

    assert (
        tmp_path
        / "gunit"
        / "modules"
        / "trade_engine.py"
    ).exists()

    assert (
        tmp_path
        / "tests"
        / "unit"
        / "test_trade_engine.py"
    ).exists()