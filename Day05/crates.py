"""
Allister MacLeod - Advent of Code 2022
Day 5 - cargo crate stacks and crane

"""

from __future__ import annotations

import re


def columns(line: str, width: int) -> list[str]:
    pieces = []
    for i in range(0, len(line), width):
        pieces.append(line[i:i+width])
    return pieces


def crate_row(line: str) -> list[str]:
    cols = columns(line, 4)
    return [parse_crate(col) for col in cols]


def parse_crate(crate_def: str) -> str:
    crate = crate_def.strip()
    if len(crate) > 1:  # expecting '[X]'
        return crate[1]


def parse_stacks(lines: list[str]) -> list[CrateStack]:
    rows = []
    for line in lines:
        if '[' not in line:
            break
        rows.append(crate_row(line))
    dock_width = max([len(row) for row in rows])
    stacks = []
    for i in range(dock_width):
        stacks.append(CrateStack())
    for row in reversed(rows):
        for i, crate in enumerate(row):
            if crate is not None:
                stacks[i].add(crate)
    return stacks


def parse_moves(lines: list[str]) -> list[MoveInstruction]:
    instructions = []
    for line in lines:
        if not line.startswith('move'):
            continue
        instructions.append(parse_move(line.strip()))
    return instructions


MOVE_PATTERN = re.compile(r'move (\d+) from (\d+) to (\d+)')
def parse_move(instruction: str) -> MoveInstruction:
    match = MOVE_PATTERN.fullmatch(instruction)
    source = int(match[2]) - 1
    target = int(match[3]) - 1
    quantity = int(match[1])
    return MoveInstruction(source=source, target=target, quantity=quantity)


def apply_move(stacks: list[CrateStack], move: MoveInstruction):
    for i in range(move.quantity):
        crate = stacks[move.source].lift()
        stacks[move.target].add(crate)


def apply_move_unified(stacks: list[CrateStack], move: MoveInstruction):
    """
    The CrateMover 9001 moves crates all at once, preserving order.

    """
    crates = stacks[move.source].lift_many(move.quantity)
    stacks[move.target].add_many(crates)


class MoveInstruction(object):
    def __init__(self, source: int, target: int, quantity: int):
        self.source = source
        self.target = target
        self.quantity = quantity


class CrateStack(object):
    """
    Representation of a single stack of crates. Crates can be added
    to or removed from the top.

    """
    def __init__(self):
        self.crates = []

    def add(self, item: str):
        self.crates.append(item)

    def top(self):
        """
        Check the top crate without moving it.
        """
        return self.crates[-1]

    def lift(self) -> str:
        return self.crates.pop()

    def lift_many(self, quantity: int) -> list[str]:
        lifted = self.crates[-quantity:]
        del(self.crates[-quantity:])
        return lifted

    def add_many(self, crates: list[str]):
        for crate in crates:
            self.add(crate)

