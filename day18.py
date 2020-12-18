#!/usr/bin/env python3

import re


def newmath(expr):
    e = expr.split()
    result = int(e[0])
    for i in e[1:]:
        if not i.isnumeric():
            op = i
        else:
            result = eval(str(result) + op + i)
    return result


assert newmath("1 + 2 * 3 + 4 * 5 + 6") == 71


def part1(expr, part2=False):
    p = re.compile(r"\(([^()]+)\)")
    while p.search(expr):
        expr = p.sub(lambda m: str(newmath(m.group(1))), expr)
    return newmath(expr)


def part2(expr):
    def plusfirst(expr):
        p = re.compile(r"(\d+ \+ \d+)")
        while p.search(expr):
            expr = p.sub(lambda m: str(eval(m.group(1))), expr)
        return eval(expr)

    p = re.compile(r"\(([^()]+)\)")
    while p.search(expr):
        expr = p.sub(lambda m: str(plusfirst(m.group(1))), expr)
    return plusfirst(expr)


with open("input18") as fp:
    lines = [line.strip() for line in fp.readlines()]

print("#1", sum(part1(line) for line in lines))
print("#2", sum(part2(line) for line in lines))


assert part1("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert part1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240

assert part2("1 + 2 * 3 + 4 * 5 + 6") == 231
assert part2("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert part2("2 * 3 + (4 * 5)") == 46
assert part2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
assert part2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
assert part2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340
