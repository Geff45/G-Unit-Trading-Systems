import sys

from forge.cli import main


def test_cli_version(monkeypatch):

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "forge",
            "version",
        ],
    )

    main()