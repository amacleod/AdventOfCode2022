"""
Allister MacLeod - Advent of Code 2022
Day 3 puzzle 1 - sum of priorities of duplicated item types

"""

import fileinput
import rucksack


def main():
    sacks = [rucksack.Sack(line) for line in fileinput.input()]
    priorities = []
    for sack in sacks:
        for duplicate in sack.duplicates():
            priority = rucksack.item_priority(duplicate)
            priorities.append(priority)
    total = 0
    for priority in priorities:
        total += priority
    print(total)


if __name__ == '__main__':
    main()
