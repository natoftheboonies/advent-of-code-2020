#!/usr/bin/env python3

TARGET_SUM = 2020


def part1(numbers, target=TARGET_SUM):
    x, y = 0, len(numbers) - 1
    while x < y:
        xy = numbers[x] + numbers[y]
        if xy == target:
            return numbers[x] * numbers[y]
        elif xy < target:
            x += 1
        else:
            y -= 1


def part2(numbers):
    x = 0
    while x < len(numbers) - 3:
        target = TARGET_SUM - numbers[x]
        if part1(numbers[x + 1 :], target):
            return numbers[x] * part1(numbers[x + 1 :], target)
        x += 1


with open("input1") as fp:
    lines = [line.strip() for line in fp.readlines()]

data = list(sorted(map(int, lines)))

print("#1", part1(data))
print("#2", part2(data))
