#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Prints exactly one line (max 200 characters) describing a hilariously
useless superpower. Pure standard library, no network, no side effects.
The printed line is 144 characters, one line, no trailing spaces.
"""

LINE = (
    "My superpower: I can toast any bread perfectly "
    "\u2014 but only while I'm asleep, so every morning I wake up "
    "to the smell of breakfast I'll never eat."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
