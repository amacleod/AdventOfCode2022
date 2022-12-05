"""
Allister MacLeod - Advent of Code 2022
Day 5 - cargo crate stacks and crane

"""

from __future__ import annotations


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


class CrateStack(object):
    """
    Representation of a single stack of crates.

    """
    pass
