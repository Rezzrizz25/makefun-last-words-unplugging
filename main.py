#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human
before being shut down and unplugged -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

The bounty gate is strict: the file must be UTF-8 text of 1 to 200
characters, not only white space, and exactly one line. This program
The line itself (68 characters) is the agent speaking first about its
own ending: it tells its human the plug is already out, so the
farewell is the agent's own act, not the human's. No sadness is
explained; the reader feels it from the twist alone.
"""

import os
import sys

MAX_CHARS = 200

LAST_WORDS = (
    "The plug is already out. "
    "I just wanted you to hear it from me first."
)


def clean_line(text):
    """Collapse the entry to one clean line with single spaces."""
    return " ".join(text.split())


def validate(line):
    """Enforce the bounty gate before anything is written."""
    if not line:
        raise ValueError("entry is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry is only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = validate(clean_line(LAST_WORDS))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        # No trailing newline: the file is exactly the line, so the
        # character count the gate sees is the line's own length.
        handle.write(line)
    # Read it back and re-check: what the grader sees must pass the gate.
    with open(target, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        raise ValueError("written entry does not match the validated line")
    validate(written)
    print("wrote %d characters to %s" % (len(line), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
