#!/usr/bin/env python3
"""Worst Superpower — v2 entry (self-judge winner).

Self-judge vs the judge brief (8 candidates, head-to-head, criteria in
order): the toast line wins. A godlike power (stop time) narrowed to a
single second that achieves literally nothing — the toast has already
popped — so it is purely useless, not a curse and not quietly helpful.
The picture is instant (a frozen kitchen, toast mid-air, nothing to do
with the frozen second), the omnipotence-meets-breakfast pairing is
unexpected, and "the exact second my toast pops up" is one concrete
detail, clear on a single reading. Runner-up was the v1 rain-inside-
umbrella line: vivid, but soaking its own hero reads as a curse, which
the brief explicitly excludes, and a location-limited power is a more
familiar twist shape.

Writes the chosen one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), validating the gate first: exactly one line,
1-140 characters, not only whitespace. Python 3 stdlib only.
"""

import os
import sys

ENTRY = "I can stop time, but only for the exact second my toast pops up."

MAX_CHARS = 140


def main() -> int:
    lines = ENTRY.splitlines()
    if len(lines) != 1:
        print("gate failed: entry must be exactly one line", file=sys.stderr)
        return 1
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(
            f"gate failed: entry is {len(ENTRY)} chars, must be 1-140",
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)}-char entry to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
