#!/usr/bin/env python3
"""One Star for Monday - make.fun entry.

The program writes the entrant's single one-star review of Monday,
written as though Monday were a restaurant, to /output/entry.txt:
at most 25 words of plain text. The line is a fixed string, so every
run writes byte-identical output.

The joke is the service complaint: Monday the waiter pockets the
weekend and never brings the bill.
"""

import os

ENTRY = "One star. Arrived cold, no atmosphere, and the waiter, Monday himself, took my weekend and never brought the bill. Would not return."


def main() -> None:
    """Write the one-line review to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
