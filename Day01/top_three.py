"""
Allister MacLeod - Advent of Code 2022
Day 1, Puzzle 2 - Elf Calories Top Three

"""

import fileinput


def main():
    elves = []
    calories = 0
    for line in fileinput.input():
        stripped_line = line.strip()
        if len(stripped_line) == 0 and calories > 0:
            elves.append(calories)
            calories = 0
        else:
            calories += int(stripped_line)
    if calories > 0:
        elves.append(calories)
    elves.sort(reverse=True)
    sum_top_three = elves[0] + elves[1] + elves[2]
    print(sum_top_three)


if __name__ == '__main__':
    main()
