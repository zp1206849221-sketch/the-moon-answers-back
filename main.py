#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun contest entry.

Writes one line to /output/entry.txt: the Moon, after four billion
years of wishes, howls and late-night promises, finally replies.
"""

import os

LINE = (
    "Four billion years of wishes, werewolf howls, and 3 a.m. promises nobody kept, "
    "and not one of you down there has ever asked how I'm doing. "
    "I'm fine. I'm a rock. But still."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
