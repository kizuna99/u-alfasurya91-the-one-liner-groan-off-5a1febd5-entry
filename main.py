# SPDX-License-Identifier: MIT
"""The One-Liner Groan-Off — entry program.

Writes the winning line to /output/entry.txt.

The joke is a dinner-table dad pun with a double hinge: the high chair
looks down on everyone because it was "just raised that way" — raised
as in lifted up, and raised as in brought up. It won a criteria-ordered
tournament (lands as a dad joke first, then a fast punchline,
freshness, tight wording, groan quality) against eight original
candidates, including six seeded by OpenCode deepseek-v4.1-flash-free
on the Simular Box; the "ends meat" runner-up groaned well but is a
pun shape the field already knows.

Output is byte-exact, no trailing newline, inside the 1-140 char gate.
"""

from pathlib import Path

TEXT = (
    "I told the high chair to stop looking down on me; it said it "
    "was just raised that way."
)
MAX_CHARS = 140
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    assert 1 <= len(text) <= MAX_CHARS, "gate: 1 to 140 characters"
    assert text.strip(), "gate: not only whitespace"
    assert "\n" not in text, "one line only"
    assert text == text.strip()
    assert text[-1] in ".!?"
    assert "  " not in text
    assert "\t" not in text, "gate: no tab characters"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip self-check: what landed on disk must be
    # byte-identical to TEXT and still inside the gate.
    back = OUTPUT.read_bytes()
    assert back == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
