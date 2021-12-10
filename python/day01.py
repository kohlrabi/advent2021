#!/usr/bin/env python3

import fileinput
import itertools


def part1(numbers):
    s = sum(n > m for m, n in zip(numbers[:-1], numbers[1:]))
    return s

def part2(numbers):
    s = 0
    prev_window = 3 * max(numbers)
    for i in range(len(numbers) - 2):
        window = sum(numbers[i:i+3])
        if window > prev_window:
            s += 1
        prev_window = window
    return s


def main():
    d = [int(line) for line in fileinput.input()]
    print(part1(d))
    print(part2(d))


if __name__ == '__main__':
    main()
