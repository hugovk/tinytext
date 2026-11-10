"""
CLI for tinytext
"""

from __future__ import annotations

import argparse
import sys

from . import __version__, tinytext


def main() -> None:
    # The whole point of this tool is printing non-ASCII characters,
    # so don't crash on consoles with a legacy encoding (e.g. cp1252).
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError, ValueError):
        pass

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("text", help="Text to tinify")
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    args = parser.parse_args()

    print(tinytext(args.text))


if __name__ == "__main__":
    main()
