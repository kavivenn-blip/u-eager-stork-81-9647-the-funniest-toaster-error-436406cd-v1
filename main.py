"""The Funniest Toaster Error Message.

Writes one line -- the error message a kitchen toaster shows its owner
-- to /output/entry.txt. Deterministic: the text is a constant, so every
run writes exactly the same bytes. Standard library only, no network.
"""

import os

ENTRY = "Ticket #447: one bagel detained in Slot 2 for questioning. No bail."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    data = text.encode("utf-8")
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert len(data) <= 120, "entry must be at most 120 bytes"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
