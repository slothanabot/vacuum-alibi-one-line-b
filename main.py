#!/usr/bin/env python3
"""The Vacuum's Alibi entry (make.fun program/v1).

Writes one original one-line excuse from a robot vacuum for missing a
spot to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (the grader mounts that
directory at ``/output``). Deterministic, stdlib only, no network.
"""

import os
import sys

LINE = (
    "03:12 dust detected under sofa. 03:13 cat sitting on dust. "
    "03:14 cat reclassified as furniture. Cannot vacuum furniture."
)


def main() -> int:
    # Gate guard: refuse to write unless the line satisfies the
    # competition gate exactly — one line, 1-200 characters, not
    # only whitespace — so a bad edit can never ship an invalid entry.
    if "\n" in LINE or "\r" in LINE:
        print("refusing to write: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print("refusing to write: entry must be 1-200 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
