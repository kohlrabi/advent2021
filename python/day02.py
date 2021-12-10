#!/usr/bin/env python3

import fileinput
import itertools


def part1(directions):
    pos = [0, 0]
    for cmd, step in directions:
        if cmd == 'f':
            pos[0] += step
        elif cmd == 'u':
            pos[1] -= step
        elif cmd == 'd':
            pos[1] += step
    return pos[0] * pos[1]

def main():
    d = [line.split() for line in fileinput.input()]
    d = [(line[0][0], int(line[1])) for line in d]
    print(part1(d))
    #print(part2(d))


if __name__ == '__main__':
    main()
