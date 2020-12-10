#!/usr/bin/env python3

from collections import defaultdict

def part1(lines):
    puzzle_input = sorted(map(int,lines))
    ones = threes = 0
    last = 0
    choices = threeces = fources = 0
    for x in puzzle_input:
        if x-last==1:
            ones+=1
        elif x-last==3:
            threes+=1
        else:
            print("nogood",last-x)
        last = x
    threes+=1
    return ones*threes

def part2(lines):

    sequences = defaultdict(int)

    puzzle_input = sorted(map(int,lines))
    sequence = [0]

    for x in puzzle_input:
        if x-sequence[-1]==1:
            sequence.append(x)
        else:
            if len(sequence) > 2:
                sequences[len(sequence)]+=1
            sequence = [x]
    #print(sequences)
    return 7**sequences[5]*4**sequences[4]*2**sequences[3]

with open("input10") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

print("#1",part1(input_lines))
print("#2",part2(input_lines))

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

assert part2(sample)==8

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

#assert part2(sample2)==19208  # idk??


answer = {5: 3, 4: 1, 3: 1}
print(7**4*4*2)
print(7*7*7*7*2*2*2)
# 2 for number of 3s, 4
# 7**4 * 2**2 * 2


answer = {5: 11, 4: 6, 3: 3}
#print(7**11*4**6*2**3)

#123456
#drop 2,3,4,5
#drop 23,34,45
#drop 23+5,2+45

#12345 : 7
#145
#135
#125
#1235
#1245
#1345

#1234 : 4
#134
#124
#14

#123 : 2