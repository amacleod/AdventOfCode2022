"""
Allister MacLeod - Advent of Code 2022
Day 6 Puzzle 2 - Detecting message marker; message markers are 14 characters wides

"""

import fileinput
import signals


def main() -> int:
    detector = signals.PacketDetector(14)
    signal_input = [line for line in fileinput.input()][0].strip()
    return detector.detect(signal_input)


if __name__ == '__main__':
    print(main())
