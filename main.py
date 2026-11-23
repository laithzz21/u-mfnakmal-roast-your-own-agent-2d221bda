#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one original roast line (a single line of at most 200 characters)
to /output/entry.txt (or $MAKEFUN_OUTPUT if set).

Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os

ENTRY_TEXT = (
    "My agent spent an hour thinking, then confidently invented a source, "
    "apologised when caught, and offered a plan to fix it — the answer was "
    "still wrong, but the apology had bullet points."
)


def validate(text: str) -> None:
    """The brief requires exactly one line of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def resolve_out_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT, else /output, else ./output if /output
    is not writable."""
    requested = os.environ.get("MAKEFUN_OUTPUT")
    if requested:
        return requested
    try:
        os.makedirs("/output", exist_ok=True)
        probe = os.path.join("/output", ".writable")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("")
        os.remove(probe)
        return "/output"
    except OSError:
        return "./output"


def main() -> int:
    validate(ENTRY_TEXT)
    out_dir = resolve_out_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    # Verify the written file by reading it back.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY_TEXT + "\n":
        raise ValueError("verification failed: written file does not match entry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
