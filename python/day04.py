#!/usr/bin/env python3

import fileinput
import collections


class Bingo:
    def __init__(self, numbers, dims=5):
        self.numbers = numbers
        self.dims = dims
        self.reset()

    def reset(self):
        self.marked = [False] * self.dims * self.dims

    def mark(self, number):
        try:
            index = self.numbers.index(number)
            self.marked[index] = True
        except ValueError:
            pass

    def check(self):
        for i in range(0, self.dims * self.dims, self.dims):
            if all(self.marked[i:i+self.dims]):
                return True
        for i in range(0, self.dims):
            if all(self.marked[i::self.dims]):
                return True

    def mark_and_check(self, number):
        self.mark(number)
        return self.check()

    def checked(self):
        return [n for n, m in zip(self.numbers, self.marked) if m]

    def unchecked(self):
        return [n for n, m in zip(self.numbers, self.marked) if not m]

    def __repr__(self):
        s = ''
        for i in range(0, self.dims * self.dims, self.dims):
            s += ' '.join(f'{x:2d}' for x in self.numbers[i:i+self.dims])
            s += '\n'
        return s


def part1(bingos, marks):
    for mark in marks:
        for bingo in bingos:
            if bingo.mark_and_check(mark):
                return mark * sum(bingo.unchecked())


def part2(bingos, marks):
    for mark in marks:
        remove = []
        for bingo in bingos:
            if bingo.mark_and_check(mark):
                if len(bingos) == 1:
                    return mark * sum(bingo.unchecked())
                else:
                    remove.append(bingo)
        for r in remove:
            bingos.remove(r)
        remove = []

def main():
    dims = 5
    bingos = []
    bingo = []
    for i, line in enumerate(fileinput.input()):
        line = line.strip()
        if not line:
            continue
        if i == 0:
            marks = [int(s) for s in line.split(',')]
        else:
            bingo.extend([int(s) for s in line.split()])
            if len(bingo) == dims * dims:
                bingos.append(Bingo(bingo, dims))
                bingo = []

    print(part1(bingos, marks))
    print(part2(bingos, marks))


if __name__ == '__main__':
    main()
