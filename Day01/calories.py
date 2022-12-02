"""
Allister MacLeod - Advent of Code 2022
Day 1, Puzzle 1 - Elf Calories

"""

import fileinput
import logging as log

log.basicConfig()


def main():
    elves = []
    calories = 0
    for line in fileinput.input():
        if len(line.strip()) == 0 and calories > 0:
            elves.append(calories)
            calories = 0
        else:
            calories += int(line.strip())
    if calories > 0:
        elves.append(calories)
        calories = 0
    for calories_carried in elves:
        if calories_carried > calories:
            calories = calories_carried
    print(calories)


if __name__ == '__main__':
    main()
