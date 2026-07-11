"""
=============================================================
G-Unit Trading Systems (GUTS)

Developer Toolkit

File:
    main.py

Purpose:
    Entry point for the Developer Toolkit.

Version:
    0.1.0-alpha

Author:
    Geoffrey Ndungu
=============================================================
"""

from core.bootstrap import BootstrapEngine


def main():

    print("=" * 60)
    print(" G-Unit Trading Systems Developer Toolkit ")
    print("=" * 60)

    engine = BootstrapEngine()

    engine.run()


if __name__ == "__main__":
    main()