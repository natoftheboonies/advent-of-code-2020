#!/usr/bin/env python3


def parse(line):
    parts = line.strip().split()
    p_count = tuple(map(int, parts[0].split("-")))
    p_char = parts[1][0]
    password = parts[2]
    return p_count, p_char, password


def checkpass(p_count, p_char, password):
    return p_count[0] <= password.count(p_char) <= p_count[1]


def checkpass2(p_count, p_char, password):
    # password is 1-indexed
    targets = (password[p_count[0] - 1], password[p_count[1] - 1])
    return targets.count(p_char) == 1


with open("input2") as fp:
    lines = [line.strip() for line in fp.readlines()]


def part1():
    return sum([1 if checkpass(*parse(line)) else 0 for line in lines])


def part2():
    return sum([1 if checkpass2(*parse(line)) else 0 for line in lines])


print("#1", part1())
print("#2", part2())

sample = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".splitlines()

print("#sample", sum([1 if checkpass(*parse(line)) else 0 for line in sample]))
print("#sample2", sum([1 if checkpass2(*parse(line)) else 0 for line in sample]))
