#!/usr/bin/env python3

import re


def parse(data):
    sections = data.split("\n\n")
    fields = dict()  # class : ((0,1),(4,9))
    for line in sections[0].splitlines():
        field = line.split(":")[0]
        fieldranges = []
        matches = re.findall(r"(\d+-\d+)", line.strip())
        for match in matches:
            low, high = match.split("-")
            fieldranges.append((int(low), int(high)))
        fields[field] = tuple(fieldranges)

    myticket = tuple(map(int, sections[1].splitlines()[1].strip().split(",")))

    nearby = sections[2].splitlines()[1:]
    tickets = []
    for line in nearby:
        ticket = tuple(map(int, line.strip().split(",")))
        tickets.append(ticket)

    return fields, myticket, tickets


def find_invalid(fields, ticket):
    invalid = []
    for f in ticket:
        for field in fields.values():
            if any(r[0] <= f <= r[1] for r in field):
                break
        else:
            invalid.append(f)
    return invalid


def part1(data):
    fields, myticket, tickets = parse(data)
    invalid = []
    for t in tickets:
        invalid.extend(find_invalid(fields, t))
    return sum(invalid)


def valid_fields(fields, tickets, idx):
    valid = []
    for field, ranges in fields.items():
        for ticket in tickets:
            value = ticket[idx]
            if not any(r[0] <= value <= r[1] for r in ranges):
                break
        else:
            valid.append(field)
    return valid


def part2(data):
    fields, myticket, tickets = parse(data)
    alltickets = [t for t in tickets if not find_invalid(fields, t)] + [myticket]
    possible = []
    for i in range(len(myticket)):
        valid = valid_fields(fields, alltickets, i)
        possible.append(valid)
    count = 0
    while any((len(p) > 1 for p in possible)) and count < 100:
        count += 1
        # find certain fields:
        certain = [p[0] for p in possible if len(p) == 1]
        for p in possible:
            if len(p) == 1:
                continue
            for c in certain:
                if c in p:
                    p.remove(c)
    departure_product = 1
    for i, p in enumerate(possible):
        if p[0].startswith("departure"):
            departure_product *= myticket[i]
    return departure_product


with open("input16") as fp:
    puzzle = fp.read()

print("#1", part1(puzzle))
print("#2", part2(puzzle))

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

assert part1(sample) == 71

sample2 = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""
print(part2(sample2))
