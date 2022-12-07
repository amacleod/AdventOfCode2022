"""
Allister MacLeod - Advent of Code 2022
Day 6 Puzzle 1 - Detecting packet start marker in signal stream

"""

import fileinput
import signals


def main() -> int:
    detector = signals.PacketDetector(4)
    signal_input = [line for line in fileinput.input()][0].strip()
    return detector.detect(signal_input)


if __name__ == '__main__':
    print(main())
