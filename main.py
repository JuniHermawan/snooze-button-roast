"""Snooze Button Roast entry (v5, final).

One line roasting an alarm clock that rings at 6 AM on a Saturday.
Writes the line to /output/entry.txt.
Deterministic, Python 3.13 standard library only, no network.

Revision history (all in this session):
- v1: "Six AM Saturday: ..." — winning candidate of 16, scored 24/25.
- v2: names "6 AM on a Saturday" in the judge brief's own words.
- v3: tried "for one dark second" — told what "being murdered" shows.
- v4: dropped the comma after "for a second" — rushed the confession.
- v5: restores v2's comma. The beat before "I considered granting its
  wish" is what sells the punchline; one byte is worth less than the laugh.
  Final line, 133 chars, 25 words, 133 bytes — inside the 1-200 gate.
"""

import os

LINE = "My alarm clock screamed like it was being murdered at 6 AM on a Saturday, and honestly, for a second, I considered granting its wish."


def _check_gate(text):
    """Refuse to write a line the gate would reject (1-200 chars, not blank)."""
    if not text.strip() or not 1 <= len(text) <= 200:
        raise ValueError("entry line fails the 1-200 character gate")


def main():
    _check_gate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
