#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun.

Writes one original two-sentence horror story to entry.txt.
Deterministic, standard library only: the same bytes every run.
"""

import os

STORY = (
    "In every photograph my grandfather took in the war, there is one extra "
    "soldier no one in the family can name. Yesterday my son pointed at him "
    "in his birthday photo and said, 'That's the man who tucks me in.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
