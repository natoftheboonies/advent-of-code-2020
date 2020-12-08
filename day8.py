#/usr/bin/env python3


def part1(program):

    accum = 0
    ptr = 0
    count = 0
    visited = set()
    while ptr < len(program) :
        count += 1
        if ptr in visited:
            #print(ptr,accum)
            return accum
        inst, b = program[ptr]
        visited.add(ptr)
        #print(inst,b)
        if inst == 'acc':
            accum += b
        elif inst == 'jmp':
            ptr += b
            continue
        elif inst == 'nop':
            pass
        ptr += 1
    print('end',accum)


def part2(program):

    accum = 0
    ptr = 0
    count = 0
    visited = set()
    while ptr < len(program) :
        count += 1
        if ptr in visited:
            #print(ptr,accum)
            return False, -1
        inst, b = program[ptr]
        visited.add(ptr)
        #print(inst,b)
        if inst == 'acc':
            accum += b
        elif inst == 'jmp':
            ptr += b
            continue
        elif inst == 'nop':
            pass
        ptr += 1
    return True, accum

import copy

def part2wrap(program):
    for x in range(len(program)):
        inst = program[x]
        if inst[0] in ['jmp','nop']:
            test_program = copy.copy(program)
            if inst[0]=='jmp':
                test_program[x] = ('nop', inst[1])
            else:
                test_program[x] = ('jmp', inst[1])
            result = part2(test_program)
            if result[0]:
                return result[1]

with open('input8') as fp:
	lines = [line.strip() for line in fp.readlines()]

input_program = list()
for line in lines:
    inst = line.split()
    input_program.append((inst[0],int(inst[1])))

print("#1",part1(input_program))
print("#2",part2wrap(input_program))


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

sample_program = list()
for line in sample:
    inst = line.split()
    sample_program.append((inst[0],int(inst[1])))

assert part1(sample_program)==5
assert part2wrap(sample_program)==8




