"""
=============================================================
GUTS Developer Toolkit

Entry Point

Version:
    0.1.0-alpha
=============================================================
"""

from app.application import Application


def main():

    app = Application()

    app.start()


if __name__ == "__main__":
    main()