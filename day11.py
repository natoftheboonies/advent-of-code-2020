#!/usr/bin/env python3


def parse(lines):
    plane = dict()
    for y, line in enumerate(lines):
        for x, seat in enumerate(line):
            if seat == "L":
                plane[(x,y)] = seat
    return plane

from copy import deepcopy

def evolve(plane):
    plane_n = deepcopy(plane)
    for x,y in plane_n.keys():
        neighbors = 0
        for dx,dy in ([(0,1),(1,1),(1,0),(-1,1),(-1,-1),(1,-1),(0,-1),(-1,0)]):
            if plane.get((x+dx,y+dy),'.') == "#":
                neighbors += 1
        if neighbors == 0:
            plane_n[(x,y)] = '#'
        elif neighbors >= 4:
            plane_n[(x,y)] = 'L'
    return plane_n


def print_plane(plane):
    maxy = max([y for x,y in plane.keys()])
    maxx = max([x for x,y in plane.keys()])
    for y in range(maxy+1):
        for x in range(maxx+1):
            print(plane.get((x,y),'.'),end='')
        print()

def part1(plane):
    last = None
    count = list(plane.values()).count("#")
    while last != count:
        last = count
        plane = evolve(plane)
        count = list(plane.values()).count("#")
    return count



with open('input11') as fp:
    input_lines = [line.strip() for line in fp.readlines()]

plane = parse(input_lines)
print("#1",part1(plane))


sample = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".splitlines()

sample_plane = parse(sample)
assert part1(sample_plane)==37