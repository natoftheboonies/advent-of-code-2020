#!/usr/bin/env python3

from collections import defaultdict





def part1(cube):

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

    for _ in range(6):
        cube = grow(cube)
        #print(len(cube))
    return len(cube)


def part2(cube):

    def check(target, cube):
        neighbors = 0
        for y in range(-1,2):
            for x in range(-1,2):
                for z in range(-1,2):
                    for w in range(-1,2):
                        friend = (target[0]+x,target[1]+y,target[2]+z, target[3]+w)
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
        x_range = range(min(x for (x,y,z,w) in cube)-1, max(x for (x,y,z,w) in cube)+2)
        y_range = range(min(y for (x,y,z,w) in cube)-1, max(y for (x,y,z,w) in cube)+2)
        z_range = range(min(z for (x,y,z,w) in cube)-1, max(z for (x,y,z,w) in cube)+2)
        w_range = range(min(w for (x,y,z,w) in cube)-1, max(z for (x,y,z,w) in cube)+2)
        for x in x_range:
            for y in y_range:
                for z in z_range:
                    for w in w_range:
                        pos = (x,y,z,w)
                        if check(pos,cube):
                            cube_n.add(pos)
        return cube_n

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

def parse2(lines):
    cube = set()

    z = 0
    w = 0
    y_offset = len(lines)//2
    for y, line in enumerate(lines):
        x_offset = len(line)//2
        for x, c in enumerate(line):
            if c == "#":
                pos = (x-x_offset, y-y_offset, z, w)
                cube.add(pos)
    return cube

with open('input17') as fp:
    input_lines = [line.strip() for line in fp.readlines()]

print("#1",part1(parse(input_lines)))
print("#2",part2(parse2(input_lines)))

sample = """\
.#.
..#
###
""".splitlines()

assert part1(parse(sample))==112
assert part2(parse2(sample))==848



