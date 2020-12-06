#!/usr/bin/env python3

def parse_groups(lines):
    """returns a list of groups of voters and their votes"""
    groups = list()
    groups.append(list())  # first group
    for line in lines:
        if not line:  # next group
            groups.append(list())
        else:
            groups[-1].append(line)
    return groups

with open("input6") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

groups = parse_groups(input_lines)

# votes made by at least one member in a group
part1 = sum([len(set().union(*[set(person) for person in group])) for group in groups])
print("#1", part1)

# votes made by all members of a group
part2 = sum([len(set.intersection(*[set(person) for person in group])) for group in groups])
print("#2", part2)
