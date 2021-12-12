#!/usr/bin/env python3

import fileinput
import collections


class Heightmap:
    def __init__(self, heightmap):
        self.heightmap = heightmap
        self.height = len(self.heightmap)
        self.width = len(self.heightmap[0])

    def __getitem__(self, key):
        return self.heightmap[key]

    def value(self, x, y):
        return self.heightmap[y][x]

    def neighbours(self, x, y):
        valid = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        if x == 0:
            valid.remove((x-1, y))
        elif x == self.width - 1:
            valid.remove((x+1, y))
        if y == 0:
            valid.remove((x, y-1))
        elif y == self.height - 1:
            valid.remove((x, y+1))
        values = [self.value(*v) for v in valid]
        return values


def part1(heightmap):
    valid = []
    for x in range(0, heightmap.width):
        for y in range(0, heightmap.height):
            value = heightmap.value(x, y)
            neighbours = heightmap.neighbours(x, y)
            if all(n - value > 0 for n in neighbours):
                valid.append(value + 1)
    return sum(valid)


def part2(heightmap):
    pass


def main():
    heightmap = []
    for line in fileinput.input():
        if ls := line.strip():
            heightmap.append([])
            for c in ls:
                heightmap[-1].append(int(c))
    heightmap = Heightmap(heightmap)

    print(part1(heightmap))
    print(part2(heightmap))


if __name__ == '__main__':
    main()
