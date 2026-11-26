#!/usr/bin/env python3
"""One funny new name for a planet, plus the why, in a single line.

This script is the entry for the make.fun bounty "Rename the Planet".
It writes a single line — a planet's funny new name and the reason for
it — into entry.txt, byte for byte, with no trailing newline and
nothing else.

Only the Python standard library is used, so it runs on vanilla Python.
"""

import argparse
import os
import sys

LINE = "Mars is now 'Second-Hand Earth': same red dust, same broken promises, but the rent is lower and nobody has invented Mondays there yet."

CHAR_LIMIT = 200
FILENAME = "entry.txt"
DEFAULT_OUT = "/output"


def find_problems(line):
    """Collect every rule the line breaks; an empty list means it is fine."""
    problems = []
    if line == "":
        problems.append("line is blank")
    if line != line.strip():
        problems.append("line starts or ends with whitespace")
    if "\n" in line or "\r" in line:
        problems.append("line breaks across more than one line")
    if len(line) > CHAR_LIMIT:
        problems.append(
            "line is %d characters long, over the %d limit"
            % (len(line), CHAR_LIMIT)
        )
    if "  " in line:
        problems.append("line has two spaces in a row")
    if not line.endswith("."):
        problems.append("line does not end with a full stop")
    return problems


def check_line(line):
    """Raise if the line breaks any of the entry rules."""
    problems = find_problems(line)
    if problems:
        raise ValueError("; ".join(problems))


def resolve_target():
    """Work out where entry.txt should land and make sure the folder exists."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUT)
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, FILENAME)


def emit(line, path):
    """Write the line as raw bytes, without appending a newline."""
    payload = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    return payload


def confirm_written(path, expected):
    """Read the file back and insist the bytes match what we wrote."""
    with open(path, "rb") as handle:
        stored = handle.read()
    if stored != expected:
        raise ValueError(
            "file on disk does not match the entry (%d bytes vs %d expected)"
            % (len(stored), len(expected))
        )
    check_line(stored.decode("utf-8"))


def run(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the one-line entry to entry.txt."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="only validate the entry line, without writing any file",
    )
    args = parser.parse_args(argv)

    check_line(LINE)
    if args.check:
        print("line OK: %d characters, no problems found" % len(LINE))
        return 0

    path = resolve_target()
    payload = emit(LINE, path)
    confirm_written(path, payload)
    print("wrote %d bytes to %s" % (len(payload), path))
    return 0


if __name__ == "__main__":
    sys.exit(run())
