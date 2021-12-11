#!/usr/bin/env python3

import fileinput
import collections


def part1(fishes, days=80):
    maxpos = max(fishes)
    least = float('inf')
    for i in range(0, maxpos+1):
        s = sum(abs(i - fish) for fish in fishes)
        least = min(s, least)
    return least

def part2(fishes):
    maxpos = max(fishes)
    costs = [0]
    for i in range(1, maxpos+1):
        costs.append(costs[-1] + i)
        
    least = float('inf')
    for i in range(0, maxpos+1):
        s = sum(costs[abs(i - fish)] for fish in fishes)
        least = min(s, least)
    return least

def main():
    for line in fileinput.input():
        crabs = [int(x) for x in line.strip().split(',')]
        
    print(part1(crabs))
    print(part2(crabs))


if __name__ == '__main__':
    main()
