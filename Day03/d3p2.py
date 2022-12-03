"""
Allister MacLeod - Advent of Code 2022
Day 3 Puzzle 2 - Elf rucksack badges

"""

import fileinput
import rucksack


def main():
    sacks = [rucksack.Sack(line) for line in fileinput.input()]
    groups = []
    group = []
    for sack in sacks:
        group.append(sack)
        if len(group) >= 3:
            groups.append(group)
            group = []
    badges = []
    for group in groups:
        matches_ab = group[0].matches(group[1])
        matches_ac = group[0].matches(group[2])
        badge = matches_ab.intersection(matches_ac)
        assert(len(badge) == 1)
        badges.append(badge.pop())
    total = sum([rucksack.item_priority(badge) for badge in badges])
    print(total)


if __name__ == '__main__':
    main()
