#!/usr/bin/env python3

import re


def part1(lines):
    def apply_mask(mask, value):
        value_b = format(value, "036b")
        for i, c in enumerate(mask):
            if c in "01":
                value_b = value_b[:i] + c + value_b[i + 1 :]
        return int(value_b, 2)

    memory = dict()
    mask = None
    for line in lines:
        left, right = line.split(" = ")
        if left == "mask":
            mask = right
            continue
        value = int(right)
        g = re.search(r"\[(\d+)\]", left)
        addr = int(g.group(1))
        memory[addr] = apply_mask(mask, value)
    return sum(memory.values())


def part2(lines):
    def apply_mask(mask, value):
        value_b = format(value, "036b")
        for i, c in enumerate(mask):
            if c in "1X":
                value_b = value_b[:i] + c + value_b[i + 1 :]
        return value_b

    def expand_floating(value_b):
        if "X" in value_b:
            i = value_b.index("X")
            rest = expand_floating(value_b[i + 1 :])  # list
            expanded = list()
            expanded.extend((value_b[:i] + "0" + r for r in rest))
            expanded.extend((value_b[:i] + "1" + r for r in rest))
            # print(value_b, "expanded to",expanded)
            return expanded
        else:
            return [value_b]

    def find_addresses(mask, value):
        value_b = apply_mask(mask, value)
        addresses_b = expand_floating(value_b)
        return list(int(addr) for addr in addresses_b)

    memory = dict()
    mask = None
    for line in lines:
        left, right = line.split(" = ")
        if left == "mask":
            mask = right
            continue
        value = int(right)
        g = re.search(r"\[(\d+)\]", left)
        addr_start = int(g.group(1))
        for addr in find_addresses(mask, addr_start):
            memory[addr] = value
    return sum(memory.values())


with open("input14") as fp:
    lines = [line.strip() for line in fp.readlines()]

print("#1", part1(lines))
print("#2", part2(lines))

sample = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".splitlines()

assert part1(sample) == 165

sample2 = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".splitlines()

assert part2(sample2) == 208
