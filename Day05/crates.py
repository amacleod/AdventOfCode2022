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


def parse_stacks(lines: list[str]) -> list[CrateStack]:
    for line in lines:
        pass


class CrateStack(object):
    """
    Representation of a single stack of crates.

    """
    pass
