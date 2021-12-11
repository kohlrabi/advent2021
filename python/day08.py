#!/usr/bin/env python3

import fileinput
import collections

dig2seg = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

seg2dig = {
    2: (1,),
    3: (7,),
    4: (4,),
    5: (2, 3, 5,),
    6: (0, 6,),
    7: (8,)
}



def part1(all_numbers):
    s = 0
    for allnums in all_numbers:
        for num in allnums:
            dig = seg2dig[len(num)]
            if len(dig) == 1:
                s += 1
    return s

def part2(numbers):
    pass

def main():
    all_digits = []
    all_numbers = []
    for line in fileinput.input():
        digits, numbers = line.strip().split('|')
        digits = digits.strip().split()
        numbers = numbers.strip().split()
        all_digits.append(digits)
        all_numbers.append(numbers)
        
    print(part1(all_numbers))
    print(part2(all_numbers))


if __name__ == '__main__':
    main()
