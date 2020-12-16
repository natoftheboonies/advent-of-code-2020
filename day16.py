#!/usr/bin/env python3

import re

def parse(data):
    sections = data.split("\n\n")
    ranges = []
    for line in sections[0].splitlines():
        matches = re.findall(r"(\d+-\d+)",line.strip())
        for match in matches:
            low, high = match.split("-")
            ranges.append((int(low),int(high)))

    nearby = sections[2].splitlines()[1:]
    fieldvals = []
    for line in nearby:
        fieldvals.extend(map(int,line.strip().split(",")))

    return ranges, fieldvals


def part1(data):
    ranges, fieldvals = parse(data)
    invalid = []
    for v in fieldvals:
        for r in ranges:
            if r[0] <= v <= r[1]:
                break
        else:
            invalid.append(v)

    return sum(invalid)


with open('input16') as fp:
    puzzle = fp.read()

print("#1",part1(puzzle))

sample = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

assert part1(sample)==71