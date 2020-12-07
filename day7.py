#!/usr/bin/env python3

MYBAG = "shiny gold"


def parse_rules(lines):
    """parse lines into dict {'aaaaa': [(3, 'bbbb'), (2 'cccc')]}"""
    rules = dict()
    for line in lines:
        left, right = line.split(" contain ")
        left = " ".join(left.split()[:-1])
        right = right.split(", ")
        contents = list()
        for r in right:
            r = r.split()
            if r[0].isnumeric():
                contents.append((int(r[0]), " ".join(r[1:-1])))
        rules[left] = contents

    return rules


def part1(rules):
    """search for bags contaning MYBAG directly or indirectly"""
    queue = [MYBAG]
    match = set()
    while queue:
        search = queue.pop()
        for k, v in rules.items():
            if any(bag == search for _, bag in v):
                match.add(k)
                queue.append(k)
    return len(match)


def part2(rules):
    """count bags MYBAG contains directly or indirectly"""

    def numbags(search):
        count = 0
        for qty, bag in rules[search]:
            count += qty
            count += qty * numbags(bag)
        return count

    return numbags(MYBAG)


with open("input7") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

rules = parse_rules(input_lines)
print("#1", part1(rules))
print("#2", part2(rules))

sample = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".splitlines()

sample_rules = parse_rules(sample)
assert part1(sample_rules) == 4
assert part2(sample_rules) == 32
