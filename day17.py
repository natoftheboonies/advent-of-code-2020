#!/usr/bin/env python3

from itertools import product


def solve(cube, part2=False):
    if part2:
        potential = list(product((-1, 0, 1), repeat=4))
    else:
        potential = list(((*foo, 0) for foo in product((-1, 0, 1), repeat=3)))
    potential.remove((0, 0, 0, 0))

    def check(target, cube, friends=None):
        neighbors = 0
        for x, y, z, w in potential:
            friend = (target[0] + x, target[1] + y, target[2] + z, target[3] + w)
            if friends is not None:
                friends.add(friend)
            if friend in cube:
                neighbors += 1
        if target in cube:
            if neighbors in (2, 3):
                return True
            return False
        elif neighbors == 3:
            return True
        return False

    def grow(cube):
        cube_n = set()
        also_check = set()
        for pos in cube:
            if check(pos, cube, also_check):
                cube_n.add(pos)
        for pos in also_check - cube:
            if check(pos, cube):
                cube_n.add(pos)
        return cube_n

    for _ in range(6):
        cube = grow(cube)
    return len(cube)


def parse(lines):
    cube = set()
    w = z = 0
    y_offset = len(lines) // 2
    for y, line in enumerate(lines):
        x_offset = len(line) // 2
        for x, c in enumerate(line):
            if c == "#":
                pos = (x - x_offset, y - y_offset, z, w)
                cube.add(pos)
    return cube


with open("input17") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

print("#1", solve(parse(input_lines)))
print("#2", solve(parse(input_lines), True))

sample = """\
.#.
..#
###
""".splitlines()

assert solve(parse(sample)) == 112
assert solve(parse(sample),True) == 848
