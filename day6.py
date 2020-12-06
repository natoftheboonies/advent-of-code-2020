#!/usr/bin/env python3

def parse_groups(lines):
    """returns a list of groups of voters and their votes as a set"""
    groups = list()
    groups.append(list())  # first group
    for person in lines:
        if not person:  # next group
            groups.append(list())
        else:
            groups[-1].append(set(person))
    return groups

with open("input6") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

groups = parse_groups(input_lines)

# votes made by at least one member in a group
part1 = sum([len(set().union(*group)) for group in groups])
print("#1", part1)

# votes made by all members of a group
part2 = sum([len(set.intersection(*group)) for group in groups])
print("#2", part2)
