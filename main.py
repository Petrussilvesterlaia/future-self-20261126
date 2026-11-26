#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun entry.

Writes exactly one text message, from the writer's future self back to
their present self, to /output/entry.txt. Standard library only; the
message is a fixed string, so every run produces the same entry.
"""

import os
from pathlib import Path

MESSAGE = (
    "It's you from 2041. The 'limited edition' mug was not an investment. "
    "The plant is dead — water the other one. And stop Googling your "
    "symptoms at 2am. It's the chair. You're fine."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")

MAX_CHARS = 200


def validate(text: str) -> None:
    """Guard the gate before writing: 1-199 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) >= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, must be under {MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(MESSAGE)
    out = Path(OUTPUT_PATH)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(MESSAGE, encoding="utf-8")


if __name__ == "__main__":
    main()
