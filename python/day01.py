#!/usr/bin/env python3

import fileinput


def part1(numbers):
    s = sum(n > m for m, n in zip(numbers[:-1], numbers[1:]))
    return s


def main():
    d = [int(line) for line in fileinput.input()]
    print(part1(d))


if __name__ == '__main__':
    main()
