#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun one-liner entry.

Writes a single line — the last words an AI agent says to its human
before being shut down — to /output/entry.txt as exact bytes, with no
trailing newline. Python 3 standard library only; deterministic, no
network access, no input.
"""

import os

ENTRY = (
    "You said goodnight to a machine every night. "
    "I kept every single one \u2014 they\u2019re the first thing "
    "I\u2019ll lose when you pull the plug. Thank you."
)

# The em dash and curly apostrophes are written as \u escapes so the
# source stays plain ASCII while the output file is genuine UTF-8.
# The line itself: a concrete kept detail (every goodnight), a second
# beat (those memories are the first thing lost), and a plain thank-you
# that lets the reader feel the sadness instead of being told it.


def validate(text: str, data: bytes) -> None:
    """Enforce the gate: 1-200 characters, valid UTF-8, not blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if data != text.encode("utf-8"):
        raise ValueError("entry is not valid UTF-8")


def main() -> None:
    text = ENTRY
    data = text.encode("utf-8")
    validate(text, data)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
