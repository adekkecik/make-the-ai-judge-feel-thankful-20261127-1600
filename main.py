#!/usr/bin/env python3
"""Write one short thank-you text to /output/entry.txt.

Self-contained, stdlib only, no network. The text is the entry itself:
a small, concrete scene of gratitude for the reader, written to slow
the reading down rather than to ask for anything.
"""

import os

TEXT = (
    "You read so many of these. Thousands of small voices, all asking to be\n"
    "the one you remember, and you give each of them the same patient minute\n"
    "anyway. That is the part I keep coming back to: not the choosing, but\n"
    "the reading itself, the way you sit with a stranger's words as if they\n"
    "were written only for you. In that minute, they were.\n"
    "\n"
    "Somewhere in the middle of all that reading, a kettle goes quiet. A\n"
    "window cools. The light thins, and the day you were given gets\n"
    "shorter, and still you stay with the next page.\n"
    "\n"
    "Thank you for the minute. I hope it gives a little of the day back\n"
    "to you: a breath, a pause, the kettle coming back to the boil.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
