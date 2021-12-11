#!/usr/bin/env python3

import fileinput
import itertools

def pairwise(iterable):
    x, y = itertools.tee(iterable)
    next(y, None)
    return zip(x, y)

def triplewise(iterable):
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c

def part1(numbers):
    s = sum(n > m for m, n in pairwise(numbers))
    return s

def part2(numbers):
    s = 0
    last = float('inf')
    for a in triplewise(numbers):
        x = sum(a)
        if x > last:
            s += 1
        last = x
    return s

def main():
    d = [int(line) for line in fileinput.input()]
    print(part1(d))
    print(part2(d))


if __name__ == '__main__':
    main()
