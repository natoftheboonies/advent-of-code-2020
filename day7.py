#!/usr/bin/env python3

from collections import defaultdict

with open("input7") as fp:
    input_lines = [line.strip() for line in fp.readlines()]


def parse_rules(lines):
    rules = dict()
    for line in lines:
        left, right = line.split(" contain ")
        left = ' '.join(left.split()[:-1])
        right = right.split(", ")
        contents = list()
        for r in right:
            r = r.split()
            if r[0].isnumeric():
                contents.append((int(r[0]),' '.join(r[1:3])))
        rules[left] = contents

    return rules


def part1(rules):
    search = 'shiny gold'

    def searchfor(search):
        match = set()
        for k, v in rules.items():
            if any(bag == search for _, bag in v):

                match.add(k)
                for j in searchfor(k):
                    match.add(j)
        return match

    return len(searchfor(search))

def part2(rules):
    search = 'shiny gold'

    def numbags(search):
        count = 0
        for qty, bag in rules[search]:
            count += qty
            #print("+",qty,bag)
            count += qty*numbags(bag)
        return count

    return numbags(search)

rules = parse_rules(input_lines)
print("#1",part1(rules)) # not 15, not 21
print("#2",part2(rules))

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

rules = parse_rules(sample)
assert part1(rules)==4
assert part2(rules)==32






