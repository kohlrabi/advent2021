#!/usr/bin/env python3

import fileinput
import collections
import re

class Vertex:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def dx(self):
        if self.x1 == self.x2:
            return 0
        elif self.x1 < self.x2:
            return 1
        else:
            return -1
    
    def dy(self):
        if self.y1 == self.y2:
            return 0
        elif self.y1 < self.y2:
            return 1
        else:
            return -1
    
    def horizontal(self):
        return self.dy() == 0

    def vertical(self):
        return self.dx() == 0

    def straight(self):
        return self.horizontal() or self.vertical()

    def coordinates(self):
        x, y = self.x1, self.y1
        end = self.x2, self.y2
        dx, dy = self.dx(), self.dy()

        while True:
            yield x, y
            if (x, y) == end:
                break
            x += dx
            y += dy

    def __repr__(self):
        s = f'{self.x1},{self.y1} -> {self.x2},{self.y2}'
        return s


def part1(vertices):
    m = collections.defaultdict(lambda: 0)
    for vertex in vertices:
        if vertex.straight():
            for c in vertex.coordinates():
                m[c] += 1
    return sum(x >= 2 for x in m.values())
    

def part2(vertices):
    m = collections.defaultdict(lambda: 0)
    for vertex in vertices:
        for c in vertex.coordinates():
            m[c] += 1
    return sum(x >= 2 for x in m.values())

def main():
    vertices = []
    for line in fileinput.input():
        m = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line.strip())
        m = (int(x) for x in m.groups())
        v = Vertex(*m)
        vertices.append(v)

    print(part1(vertices))
    print(part2(vertices))


if __name__ == '__main__':
    main()
