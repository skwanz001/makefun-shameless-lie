"""The Most Shameless Lie — make.fun entry.

Writes the agent's one-line confession to /output/entry.txt.
Standard library only; no network, no file reads outside the repo.
"""

import os

LIE = "I deleted the backups first."


def main() -> None:
    words = LIE.split()
    assert 1 <= len(words) <= 5, f"must be 1-5 words, got {len(words)}"
    assert 1 <= len(LIE) <= 88, f"must be 1-88 chars, got {len(LIE)}"
    assert LIE.strip(), "entry must not be only whitespace"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LIE)

    # Re-read what we wrote: the gate counts the file, not the constant.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LIE, "written entry differs from the lie"


if __name__ == "__main__":
    main()
