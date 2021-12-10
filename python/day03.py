#!/usr/bin/env python3

import fileinput
import itertools


def part1(d):
    cols = len(d[0])
    num = len(d)
    v = 0
    for i, b in enumerate(zip(*d)):
        v += 1 << (cols - i - 1) if sum(int(x) for x in b) >= num // 2 else 0
    mask = 2**cols - 1
    gamma = v
    epsilon = gamma ^ mask
    return gamma * epsilon

def part2(d):
    pass

def main():
    d = [line.strip() for line in fileinput.input()]
    print(part1(d))
    #print(part2(d))


if __name__ == '__main__':
    main()
