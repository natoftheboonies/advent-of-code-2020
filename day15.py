#!/usr/bin/env python3


def play(start, until):
    history = dict()
    turn = 0
    last = -1
    for i in start:
        turn += 1
        if last >= 0:
            history[last] = turn - 1
        last = i
    while turn < until:
        cur = 0
        if last in history:
            cur = turn - history[last]
        history[last] = turn
        turn += 1
        # print(f"turn {turn} plays {cur}")
        last = cur
    return last


sample = [0, 3, 6]
assert play(sample, 2020) == 436

puzzle = [8, 13, 1, 0, 18, 9]
print("#1", play(puzzle, 2020))
print("#2", play(puzzle, 30000000))
