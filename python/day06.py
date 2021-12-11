#!/usr/bin/env python3

import fileinput
import collections


def part1(fishes_input, days=80):
    fishes = {x: 0 for x in range(0, 9)}
    for fish in fishes_input:
        fishes[fish] += 1

    for _ in range(days):
        new = fishes[0]
        fishes = {key-1: value for key, value in fishes.items() if key != 0}
        fishes[8] = new
        fishes[6] += new

    return sum(fishes.values())

def part2(fishes):
    return part1(fishes, 256)

def main():
    for line in fileinput.input():
        fishes = [int(x) for x in line.strip().split(',')]
        
    print(part1(fishes))
    print(part2(fishes))


if __name__ == '__main__':
    main()
