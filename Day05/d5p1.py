"""
Allister MacLeod - Advent of Code 2022
Day 5 Puzzle 1 - cranes moving crates

"""

import fileinput
import crates


def main() -> str:
    lines = [line for line in fileinput.input()]
    stacks = crates.parse_stacks(lines)
    moves = crates.parse_moves(lines)
    for move in moves:
        crates.apply_move(stacks, move)
    top_crates = [stack.top() for stack in stacks]
    return ''.join(top_crates)


if __name__ == '__main__':
    print(main())
