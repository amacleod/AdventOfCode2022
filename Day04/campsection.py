"""
Allister MacLeod - Advent of Code 2022
Day 4 module - camp sections and ranges thereof

"""

from __future__ import annotations


def parse_elf_pairs(lines: list[str]) -> list[(CampSectionRange, CampSectionRange)]:
    return [parse_pair(line) for line in lines]


def parse_pair(pair_def: str) -> (CampSectionRange, CampSectionRange):
    first, second = pair_def.split(',')
    return parse_range(first), parse_range(second)


def parse_range(range_def: str) -> CampSectionRange:
    (low, high) = range_def.split('-')
    return CampSectionRange(int(low), int(high))


class CampSectionRange(object):
    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper

    def fully_contains(self, other: CampSectionRange) -> bool:
        return self.lower <= other.lower and self.upper >= other.upper

    def overlaps(self, other: CampSectionRange) -> bool:
        # my tail overlaps if my upper is inside the other OR if I wholly contain the other
        tail_overlap: bool = other.lower <= self.upper <= other.upper
        # my head overlaps if my lower is inside the other OR if I wholly contain the other
        head_overlap: bool = other.lower <= self.lower <= other.upper
        return tail_overlap or head_overlap or self.fully_contains(other)
