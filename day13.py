#!/usr/bin/env python3

def part1(wait, buses):
    waiting, bus = min(((wait // bus + 1) * bus - wait, bus) for bus in buses)
    return waiting * bus


def parse(lines):
    wait = int(lines[0])
    buses = list(map(int, (bus for bus in lines[1].split(",") if bus != "x")))
    return wait, buses


def part2(buses):
    time = 0
    ticks = 1  # which times to check?
    for bus in buses:
        offset = buses[bus]
        # find next time where bus leaves after offset
        while (time + offset) % bus != 0:
            time += ticks
        ticks *= bus
        #print("bus", bus, "leaves at", time)
    return time


def parse2(line):
    schedule = line.split(",")
    buses = dict()
    for i, bus in enumerate(schedule):
        if bus != "x":
            buses[int(bus)] = i
    return buses


with open("input13") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

print("#1", part1(*parse(input_lines)))
print("#2", part2(parse2(input_lines[1])))


sample = """\
939
7,13,x,x,59,x,31,19
""".splitlines()

assert part1(*parse(sample)) == 295
assert part2(parse2(sample[1])) == 1068781

assert part2(parse2("17,x,13,19")) == 3417
assert part2(parse2("67,x,7,59,61")) == 779210
