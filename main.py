#!/usr/bin/env python3
"""Make.fun entry — Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (<=280 chars) recalling a childhood memory to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

LINE = (
    "Every August evening my grandmother called us in from the yard by "
    "rattling the old biscuit tin of fried shallots, and we came running "
    "barefoot across the still-warm tiles, certain that summer, and she, "
    "would never end."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
