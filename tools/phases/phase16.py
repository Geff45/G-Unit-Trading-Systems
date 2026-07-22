"""
Phase 16

Creates the Forge CLI.
"""


def run(g):

    # ------------------------
    # folders
    # ------------------------

    g.mkdir("tools")
    g.mkdir("tools/commands")

    # ------------------------
    # package
    # ------------------------

    g.write(
        "tools/commands/__init__.py",
        ""
    )

    # ------------------------
    # forge.py
    # ------------------------

    g.write(
        "tools/forge.py",
        '''
from pathlib import Path
import typer

from commands.phase import phase

app = typer.Typer()

app.command()(phase)

if __name__ == "__main__":
    app()
'''
    )

    # ------------------------
    # phase command
    # ------------------------

    g.write(
        "tools/commands/phase.py",
        '''
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]


def phase(number: int):

    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "update.py"),
            str(number),
        ],
        check=True,
    )
'''
    )

    # ------------------------
    # placeholders
    # ------------------------

    placeholders = [
        "build",
        "doctor",
        "package",
        "class_",
        "service",
        "event",
        "test",
    ]

    for name in placeholders:

        g.write(
            f"tools/commands/{name}.py",
            f'''
def {name.replace("-", "_")}():

    print("{name} command coming soon")
'''
        )