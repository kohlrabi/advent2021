#!/usr/bin/env python3

import fileinput
import collections


def part1(d):
    gamma = []
    epsilon = []

    for b in zip(*d):
        counter = collections.Counter(b)
        (most, _), (least, _) = counter.most_common()
        gamma.append(most)
        epsilon.append(least)

    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    
    return gamma * epsilon

def part2(d):
    cols = len(d[0])
    oxy = d[:]
    co2 = d[:]
    
    for c in range(cols):
        if(len(oxy)) == 1:
            break
        counter = collections.Counter(x[c] for x in oxy)
        common = counter.most_common()
        if len(common) == 1:
            v, _ = common[0]
        else:
            (v, cv), (w, cw) = common
            if cv == cw:
                v = '1'
        oxy = [n for n in oxy if n[c] == v]

    for c in range(cols):
        if(len(co2)) == 1:
            break
        counter = collections.Counter(x[c] for x in co2)
        common = counter.most_common()
        if len(common) == 1:
            w, _ = common[0]
        else:
            (v, cv), (w, cw) = counter.most_common()
            if cv == cw:
                w = '0'
        co2 = [n for n in co2 if n[c] == w]

    return int(oxy[0], 2) * int(co2[0], 2)

def main():
    d = [line.strip() for line in fileinput.input()]
    print(part1(d))
    print(part2(d))


if __name__ == '__main__':
    main()
