#!/usr/bin/env python3
"""Hello, World! -- with flare. Pure stdlib, terminal edition.

Run: python3 hello_world.py
"""
import sys
import time

COLORS = [
    "\033[91m",  # red
    "\033[93m",  # yellow
    "\033[92m",  # green
    "\033[96m",  # cyan
    "\033[94m",  # blue
    "\033[95m",  # magenta
]
BOLD = "\033[1m"
RESET = "\033[0m"
CLEAR_LINE = "\033[2K\r"


def typewriter(text, delay=0.045):
    for i, ch in enumerate(text):
        sys.stdout.write(COLORS[i % len(COLORS)] + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def compass_spin(frames=12, delay=0.09):
    # Scout's compass, obviously -- one that only points one way: awesome.
    arrows = ["\u2191", "\u2197", "\u2192", "\u2198",
              "\u2193", "\u2199", "\u2190", "\u2196"]
    for i in range(frames):
        sys.stdout.write(CLEAR_LINE + COLORS[i % len(COLORS)] + BOLD +
                         "    \u27a2 calibrating compass... " +
                         arrows[i % len(arrows)] + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(CLEAR_LINE + COLORS[3] + BOLD +
                     "    \u27a2 compass locked on: GREATNESS \u2191" + RESET + "\n")


def confetti_burst(rows=4):
    glyphs = ["*", "+", "o", ".", "\u2726", "\u2727", "\u2665"]
    for r in range(rows):
        line = "    "
        for c in range(36):
            g = glyphs[(r * 7 + c * 3) % len(glyphs)]
            line += COLORS[(r + c) % len(COLORS)] + g + RESET
        print(line)
        time.sleep(0.08)


def main():
    banner = [
        r" _   _      _ _         __        __         _     _ _ ",
        r"| | | | ___| | | ___    \ \      / /__  _ __| | __| | |",
        r"| |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |",
        r"|  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|",
        r"|_| |_|\___|_|_|\___/      \_/\_/ \___/|_|  |_|\__,_(_)",
    ]
    for i, line in enumerate(banner):
        print(COLORS[i % len(COLORS)] + BOLD + line + RESET)
        time.sleep(0.1)
    print()

    typewriter("Hello, World!", delay=0.09)
    print()

    compass_spin()
    print()

    print(BOLD + "    This is no ordinary greeting." + RESET)
    time.sleep(0.3)
    print(BOLD + "    It's a greeting with " +
          COLORS[1] + "f" + COLORS[0] + "l" + COLORS[5] + "a" +
          COLORS[4] + "i" + COLORS[3] + "r" + RESET + BOLD + "." + RESET)
    print()
    time.sleep(0.4)

    confetti_burst()

    print()
    sys.stdout.write(BOLD + COLORS[3] +
                     "    \U0001f9ed Hello, World says: mission accomplished." +
                     RESET + "\n")
    time.sleep(0.2)
    print(BOLD + "    (Scout was here.)" + RESET)


if __name__ == "__main__":
    main()
