# /usr/bin/env python3

from collections import deque
from itertools import combinations


def solve(sequence, preamble):
    for i in range(preamble, len(sequence)):
        num = sequence[i]
        if not any(a + b == num for a, b in combinations(sequence[i - preamble : i], 2)):
            return num


def part2(sequence, target):
    working = deque(sequence[0:2])
    i = 2
    while sum(working) != target and i < len(sequence):
        while sum(working) > target:
            working.popleft()
        while sum(working) < target:
            working.append(sequence[i])
            i += 1
    return min(working) + max(working)


with open("input9") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

input_sequence = list(map(int, input_lines))
part1 = solve(input_sequence, 25)
print("#1", part1)
print("#2", part2(input_sequence, part1))


sample = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".splitlines()

sample_sequence = list(map(int, sample))
assert solve(sample_sequence, 5) == 127
assert part2(sample_sequence, 127) == 62
