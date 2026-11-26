#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Writes a single line (at most 120 characters): the excuse a robot vacuum
gives for missing a spot. Output goes to /output/entry.txt, or to
$OUTPUT_DIR/entry.txt when OUTPUT_DIR is set.
"""

import os

ENTRY = "The dog shed 412 hairs as a peace offering. I accepted. The corner can wait."
assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
