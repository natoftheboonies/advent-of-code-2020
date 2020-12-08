# /usr/bin/env python3

import copy


def part1(program):
    accum = 0
    ptr = 0
    visited = set()
    while ptr < len(program):
        if ptr in visited:
            return accum
        inst, b = program[ptr]
        visited.add(ptr)
        if inst == "jmp":
            ptr += b
            continue
        if inst == "acc":
            accum += b
        # else nop
        ptr += 1
    raise RuntimeError("Program end")


def part2(program):
    def run_program(program):
        accum = 0
        ptr = 0
        visited = set()
        while ptr < len(program):
            if ptr in visited:
                raise RuntimeError("Program loop")
            inst, b = program[ptr]
            visited.add(ptr)
            if inst == "jmp":
                ptr += b
                continue
            if inst == "acc":
                accum += b
            # else nop
            ptr += 1
        return accum

    for ptr in range(len(program)):
        inst = program[ptr]
        if inst[0] in ["jmp", "nop"]:
            test_program = copy.copy(program)
            if inst[0] == "jmp":
                test_program[ptr] = ("nop", inst[1])
            else:
                test_program[ptr] = ("jmp", inst[1])
            try:
                return run_program(test_program)
            except RuntimeError:
                continue


def parse_program(lines):
    program = list()
    for line in lines:
        inst = line.split()
        program.append((inst[0], int(inst[1])))
    return program


with open("input8") as fp:
    lines = [line.strip() for line in fp.readlines()]
input_program = parse_program(lines)

print("#1", part1(input_program))
print("#2", part2(input_program))

sample = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".splitlines()

sample_program = parse_program(sample)

assert part1(sample_program) == 5
assert part2(sample_program) == 8
