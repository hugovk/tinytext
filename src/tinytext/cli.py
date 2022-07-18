#!/usr/bin/env python3
"""
CLI for tinytext
"""
from __future__ import annotations

import argparse

from . import __version__ as __version__
from . import tinytext


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="Text to tinify")
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    args = parser.parse_args()

    print(tinytext(args.text))


if __name__ == "__main__":
    main()
