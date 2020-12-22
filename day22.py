#!/usr/bin/env python3

from collections import deque


def parse(decks):
    players = []
    for deck in decks:
        lines = deck.splitlines()
        players.append(list(map(int, [line.strip() for line in lines[1:]])))
    return players


def score(winner):
    result = 0
    winner.reverse()
    for x in range(len(winner), 0, -1):
        result += x * winner[x - 1]
    return result


def part1(l1, l2):
    p1 = deque(l1)
    p2 = deque(l2)
    while len(p1) > 0 and len(p2) > 0:
        if p1[0] > p2[0]:
            p1.append(p1.popleft())
            p1.append(p2.popleft())
        else:
            p2.append(p2.popleft())
            p2.append(p1.popleft())

    winner = p1 if len(p1) > 0 else p2
    return score(winner)


def part2(l1, l2, subgame=False):
    p1 = deque(l1)
    p2 = deque(l2)
    prior_rounds = set()  # (tuple(p1),tuple(p2))

    while len(p1) > 0 and len(p2) > 0:
        p1_can_play = p1[0] < len(p1)
        p2_can_play = p2[0] < len(p2)
        if not (p1_can_play and p2_can_play):
            if p1[0] > p2[0]:
                win, lose = p1, p2
            else:
                win, lose = p2, p1
        else:
            sub1 = [p1[i] for i in range(1, p1[0] + 1)]
            sub2 = [p2[i] for i in range(1, p2[0] + 1)]
            if part2(sub1, sub2, True):
                win, lose = p1, p2
            else:
                win, lose = p2, p1
        win.append(win.popleft())
        win.append(lose.popleft())
        if (tuple(p1), tuple(p2)) in prior_rounds:
            # player 1 wins
            return True
        prior_rounds.add((tuple(p1), tuple(p2)))

    if subgame:
        return len(p1) > len(p2)
    else:
        return score(win)


with open("input22") as fp:
    puzzle = fp.read()

d1, d2 = parse(puzzle.split("\n\n"))
print("#1", part1(d1, d2))
print("#2", part2(d1, d2))

sample = """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".split(
    "\n\n"
)
d1, d2 = parse(sample)
assert part1(d1, d2) == 306
assert part2(d1, d2) == 291
