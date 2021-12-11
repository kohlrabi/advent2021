#!/usr/bin/env python3

import fileinput
import collections

dig2numseg = {
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

numseg2dig = {
    2: (1,),
    3: (7,),
    4: (4,),
    5: (2, 3, 5,),
    6: (0, 6,),
    7: (8,)
}

dig2segs = {
    0: ('a', 'b', 'c', 'e', 'f', 'g'),
    1: ('c', 'f'),
    2: ('a', 'c', 'd', 'e', 'g'),
    3: ('a', 'c', 'd', 'f', 'g'),
    4: ('b', 'c', 'd', 'f'),
    5: ('a', 'b', 'd', 'f', 'g'),
    6: ('a', 'b', 'd', 'e', 'f', 'g'),
    7: ('a', 'c', 'f'),
    8: ('a', 'b', 'c', 'd', 'e', 'f', 'g'),
    9: ('a', 'b', 'c', 'd', 'f', 'g'),
}

seg2digs = {
    'a': (0, 2, 3, 5, 6, 7, 8, 9),
    'b': (0, 5, 6, 8, 9),
    'c': (0, 1, 2, 3, 4, 7, 8, 9),
    'd': (2, 3, 4, 5, 6, 8, 9),
    'e': (0, 2, 6, 8),
    'f': (0, 1, 3, 4, 5, 6, 7, 8, 9),
    'g': (0, 2, 3, 5, 6, 8, 9)
}


def part1(all_numbers):
    s = 0
    for allnums in all_numbers:
        for num in allnums:
            dig = numseg2dig[len(num)]
            if len(dig) == 1:
                s += 1
    return s


def part2(all_digits, all_numbers):
    s = 0
    for digits, numbers in zip(all_digits, all_numbers):
        translation = {}

        print(digits)

        nums = {
            1: digits[0],
            7: digits[1],
            4: digits[2],
            8: digits[-1]
        }

        twothreefive = digits[3:6]
        for num in twothreefive:
            print(set(num), set(nums[1]))
            if set(num) == set(num).union(set(nums[1])):
                nums[3] = num
                break
        twothreefive.remove(nums[3])
        translation['b'] = tuple(set(nums[4]).difference(set(nums[3])))[0]

        x = set(nums[4]).difference(set(nums[1]))
        x.remove(translation['b'])
        translation['d'] = tuple(x)[0]

        for num in twothreefive:
            if 'b' in num:
                nums[5] = num
                break
        twothreefive.remove(nums[5])

        nums[2] = twothreefive[0]

        zerosixnine = digits[6:9]
        for num in zerosixnine:
            if translation['d'] not in num:
                nums[0] = num
                break
        zerosixnine.remove(nums[0])

        for num in zerosixnine:
            if set(num).union(set(nums[1])) == set(num):
                nums[9] = num
                break
        zerosixnine.remove(nums[9])

        nums[6] = zerosixnine[0]

        print(nums)

        mapping = {tuple(v): k for k, v in nums.items()}

        n = ''
        for num in numbers:
            n += str(mapping[tuple(num)])

        s += int(n)

    return s


def main():
    all_digits = []
    all_numbers = []
    for line in fileinput.input():
        digits, numbers = line.strip().split('|')
        digits = [sorted(d) for d in digits.strip().split()]
        numbers = [sorted(n) for n in numbers.strip().split()]
        all_digits.append(sorted(digits, key=lambda x: len(x)))
        all_numbers.append(numbers)

    print(part1(all_numbers))
    print(part2(all_digits, all_numbers))


if __name__ == '__main__':
    main()
