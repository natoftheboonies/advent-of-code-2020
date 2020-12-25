#!/usr/bin/env python3

from itertools import count

divisor = 20201227


def solve(search):
    subject = 7
    result = 1

    # search for both loops
    loops = []
    for i in count(1):
        result = (result * subject) % divisor
        if result in search:
            loops.append(i)
        if len(loops) == 2:
            break

    # calculate encryption key
    subject = result
    for _ in range(loops[0] - 1):
        result = (result * subject) % divisor

    return result


puzzle = (5107328, 11349501)
print("#1", solve(puzzle))

sample = (5764801, 17807724)
assert solve(sample) == 14897079
