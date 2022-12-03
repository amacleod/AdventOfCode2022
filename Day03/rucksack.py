"""
Allister MacLeod - Advent of Code
Day 3: Elf rucksacks

"""

LOWER_A = ord('a')
UPPER_A = ord('A')


def item_priority(item_type: str) -> int:
    index = ord(item_type)
    priority = index - LOWER_A + 1
    if 0 < priority < 27:
        return priority
    return index - UPPER_A + 27


class Sack(object):
    def __init__(self, line: str):
        line = line.strip()
        size = int(len(line) / 2)
        self.left = line[:size]
        self.right = line[size:]

    def duplicates(self) -> set:
        dupes = set()
        for item in self.left:
            if item in self.right:
                dupes.add(item)
        return dupes
