#!/usr/bin/env python3


with open("input6") as fp:
    input_lines = [line.strip() for line in fp.readlines()]


sample = """\
abc

a
b
c

ab
ac

a
a
a
a

b
""".splitlines()

groups = list()
group = set()
for line in input_lines:
    if not line:
        groups.append(group)
        group = set()
    else:
        for c in line:
            group.add(c)
groups.append(group)

print("#1",sum(len(group) for group in groups))

groups = list()
group = list()
for line in input_lines:
    if not line:
        groups.append(group)
        group = list()
    else:
        group.append(line)
groups.append(group)

def common(group):
    chars = set()
    for person in group:
        for c in person:
            chars.add(c)
    return sum((1 for c in chars if all(c in person for person in group)))

print("#2",sum((common(group) for group in groups)))
