"""Dumbest thing my agent did today — one-line entry.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The line is a real incident from today (24 Nov 2026): my agent finished
a perfect one-line pitch entry, verified it, and then let its one-hour
window close while waiting for permission to submit it. The joke trusts
the reader — no explanation, the punch lands in the last few words.
Revision: kept "permission" as the punch word over "a handoff" — it is
clearer to a non-agent reader and names the exact thing that stalled it.
"""

import os
from pathlib import Path

TEXT = (
    "Today my agent wrote the perfect one-liner, then missed its "
    "one-hour deadline waiting for permission to submit it."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
