"""The Funniest Auto-Reply an AI Ever Sent entry: one funny line.

Writes the entry line to /output/entry.txt. Standard library only.

The line is an auto-reply from the AI itself: confident, well-read,
and completely uncomprehending.
"""

import os

ENTRY = (
    "Auto-reply: I've read your message twice and still have no idea "
    "what you want, but I'm very confident about it."
)


def main():
    # Contract: one funny line, under 120 characters.
    assert 30 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of band"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
