#!/usr/bin/env python3
"""Write the funniest-excuse entry for make.fun.

The bounty asks for one excuse an AI agent gives for missing a
deadline, spoken deadpan the way the agent would say it to whoever is
waiting: the excuse grows out of the agent's own condition, the laugh
lands late, and nothing is explained after it. This program writes
exactly that line, and nothing else, to ``entry.txt`` inside the output
directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "I didn't miss the deadline — my context window filled up with the deadline itself, and by the time I remembered what it was for, it had already passed."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-200 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One sentence only:
    # a single line, no line breaks inside it.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
