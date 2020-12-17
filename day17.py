#!/usr/bin/env python3

from collections import defaultdict


def check(target, cube):
    neighbors = 0
    for y in range(-1,2):
        for x in range(-1,2):
            for z in range(-1,2):
                friend = (target[0]+x,target[1]+y,target[2]+z)
                if friend == target:
                    continue
                if friend in cube:
                    neighbors += 1
    if target in cube:
        if neighbors in (2,3):
            return True
        return False
    elif neighbors == 3:
        return True
    return False


def grow(cube):
    cube_n = set()
    x_range = range(min(x for (x,y,z) in cube)-1, max(x for (x,y,z) in cube)+2)
    y_range = range(min(y for (x,y,z) in cube)-1, max(y for (x,y,z) in cube)+2)
    z_range = range(min(z for (x,y,z) in cube)-1, max(z for (x,y,z) in cube)+2)
    for x in x_range:
        for y in y_range:
            for z in z_range:
                pos = (x,y,z)
                if check(pos,cube):
                    cube_n.add(pos)
    return cube_n


def part1(cube):
    for _ in range(6):
        cube = grow(cube)
        #print(len(cube))
    return len(cube)



def parse(lines):
    cube = set()

    z = 0
    y_offset = len(lines)//2
    for y, line in enumerate(lines):
        x_offset = len(line)//2
        for x, c in enumerate(line):
            if c == "#":
                pos = (x-x_offset, y-y_offset, z)
                cube.add(pos)
    return cube



with open('input17') as fp:
    input_lines = [line.strip() for line in fp.readlines()]

input_parsed = parse(input_lines)
print("#1",part1(input_parsed))

sample = """\
.#.
..#
###
""".splitlines()

assert part1(parse(sample))==112



