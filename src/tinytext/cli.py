#!/usr/bin/env python3
"""
CLI for tinytext
"""
import argparse

import tinytext


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="Text to tinify")
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {tinytext.__version__}"
    )
    args = parser.parse_args()

    print(tinytext.tinytext(args.text))


if __name__ == "__main__":
    main()
