#!/usr/bin/env python3

from collections import defaultdict
from functools import reduce
from operator import mul


def part1(lines):
    puzzle_input = sorted(map(int, lines))
    ones = threes = 0
    last = 0
    for x in puzzle_input:
        if x - last == 1:
            ones += 1
        elif x - last == 3:
            threes += 1
        last = x
    threes += 1
    return ones * threes


tribonacci_memo = {1:1}
# hint from https://www.reddit.com/r/adventofcode/comments/ka9pc3/2020_day_10_part_2_suspicious_factorisation/
def tribonacci(n):
    if n < 1:
        return 0
    if n in tribonacci_memo:
        return tribonacci_memo[n]
    
    result = 0
    for part in [n-1,n-2,n-3]:
        if part not in tribonacci_memo:
            tribonacci_memo[part] = tribonacci(part)
        result += tribonacci_memo[part]
    return result


assert tribonacci(5) == 7
print(tribonacci(13))


def part2(lines):
    sequences = defaultdict(int)

    puzzle_input = sorted(map(int, lines))
    sequence = [0]

    for x in puzzle_input:
        if x - sequence[-1] == 1:
            sequence.append(x)
        else:
            if len(sequence) > 2:
                sequences[len(sequence)] += 1
            sequence = [x]
    # add the last sequence!
    if len(sequence) > 2:
        sequences[len(sequence)] += 1

    return reduce(mul, (tribonacci(k) ** v for k, v in sequences.items()))


with open("input10") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

print("#1", part1(input_lines))
print("#2", part2(input_lines))

sample = """\
16
10
15
5
1
11
7
19
6
12
4
""".splitlines()

assert part2(sample) == 8

sample2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".splitlines()

assert part2(sample2) == 19208  # idk??


answer = {5: 4, 4: 1, 3: 1}
# print(7*7*7*7*2*2*2)


answer = {5: 11, 4: 6, 3: 3}
# print(7**11*4**6*2**3)

# 123456 : 13, but none of these...
# drop 2,3,4,5
# drop 23,34,45,24,35,25
# drop 23+5,2+45

# 12345 : 7
# drop none
# drop 2,3,4
# drop 23,34,24

# 1234 : 4
# drop none
# drop 2,3
# drop 23

# 123 : 2
# drop none, 2
