"""
Atlas Forge CLI Parser

Parses command-line arguments.

Version: 2.0.0
"""

from __future__ import annotations

import argparse


class CLIParser:

    def __init__(self):

        self._parser = argparse.ArgumentParser(
            prog="forge",
            description="Atlas Forge Developer Toolkit"
        )

        self._parser.add_argument(
            "command",
            nargs="?",
            default="help"
        )

        self._parser.add_argument(
            "arguments",
            nargs="*"
        )

    def parse(self):

        return self._parser.parse_args()