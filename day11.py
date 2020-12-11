#!/usr/bin/env python3


def parse(lines):
    plane = dict()
    for y, line in enumerate(lines):
        for x, seat in enumerate(line):
            if seat in "L#":
                plane[(x, y)] = seat
    return plane

def print_plane(plane):
    maxy = max([y for x, y in plane.keys()])
    maxx = max([x for x, y in plane.keys()])
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            print(plane.get((x, y), "."), end="")
        print()


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]


def evolve(plane, maxx, maxy, part2=False):
    def count_visible():
        neighbors = 0
        for dx, dy in DIRECTIONS:
            dist = 1
            while 0 <= x + dx * dist <= maxx and 0 <= y + dy * dist <= maxy:
                seat = plane.get((x + dx * dist, y + dy * dist), ".")
                if seat == "#":
                    neighbors += 1
                    break
                elif seat == "L":
                    break
                dist += 1
            if neighbors >= 5:
                break
        return neighbors

    def count_neighbors():
        neighbors = 0
        for dx, dy in DIRECTIONS:
            if plane.get((x + dx, y + dy), ".") == "#":
                neighbors += 1
            if neighbors >= 4:
                break
        return neighbors

    plane_n = dict()
    for x, y in plane.keys():
        neighbors = count_visible() if part2 else count_neighbors()
        threshold = 5 if part2 else 4
        if neighbors == 0:
            plane_n[(x, y)] = "#"
        elif neighbors >= threshold:
            plane_n[(x, y)] = "L"
        else:
            plane_n[(x, y)] = plane[(x, y)]
    return plane_n


def parts(plane, part2=False):
    maxy = max([y for x, y in plane.keys()])
    maxx = max([x for x, y in plane.keys()])

    last = None
    count = list(plane.values()).count("#")
    while last != count:
        last = count
        plane = evolve(plane, maxx, maxy, part2)
        count = list(plane.values()).count("#")
    return count


with open("input11") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

plane = parse(input_lines)
print("#1", parts(plane))
print("#2", parts(plane, True))


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
assert parts(sample_plane) == 37
assert parts(sample_plane, True) == 26
