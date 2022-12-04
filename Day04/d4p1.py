"""
Allister MacLeod - Advent of Code 2022
Day 4, Puzzle 1: wholly overlapping camp section ranges

"""

import fileinput
import campsection


def main() -> int:
    lines = [line for line in fileinput.input()]
    pairs = campsection.parse_elf_pairs(lines)
    full_overlaps = 0
    for left, right in pairs:
        if left.fully_contains(right) or right.fully_contains(left):
            full_overlaps += 1
    return full_overlaps


if __name__ == '__main__':
    print(main())
