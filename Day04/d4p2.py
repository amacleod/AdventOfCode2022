"""
Allister MacLeod - Advent of Code 2022
Day 4, Puzzle 2: partially overlapping camp section ranges

"""

import fileinput
import campsection


def main() -> int:
    lines = [line for line in fileinput.input()]
    pairs = campsection.parse_elf_pairs(lines)
    overlaps = 0
    for left, right in pairs:
        if left.overlaps(right):
            overlaps += 1
    return overlaps


if __name__ == '__main__':
    print(main())
