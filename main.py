#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — the fridge has had enough."""
import os

LINE = "My door alarm has gone off 12 times today. I am not broken. You are just indecisive and hungry."
assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"

def main():
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
