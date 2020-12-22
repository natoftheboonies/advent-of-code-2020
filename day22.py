#!/usr/bin/env python3

from collections import deque

def parse(decks):
    players = []
    for deck in decks:
        lines = deck.splitlines()
        players.append(list(map(int,[line.strip() for line in lines[1:]])))
    return players

def score(winner):
    result = 0
    winner.reverse()
    for x in range(len(winner),0,-1):
        result += x*winner[x-1]
    return result

def play(l1, l2):
    p1 = deque(l1)
    p2 = deque(l2)
    while (len(p1)>0 and len(p2) > 0):
        if p1[0]>p2[0]:
            p1.append(p1.popleft())
            p1.append(p2.popleft())
        else:
            p2.append(p2.popleft())
            p2.append(p1.popleft())

    winner = p1 if len(p1) > 0 else p2
    return score(winner)


def part2(l1,l2,subgame=False):
    #print("game",l1,l2)
    p1 = deque(l1)
    p2 = deque(l2)
    prior_rounds = set()  # (tuple(p1),tuple(p2))

    while (len(p1)>0 and len(p2) > 0):

        p1_can_play = p1[0] < len(p1)
        p2_can_play = p2[0] < len(p2)
        #print("players",p1_can_play,p2_can_play)

        if not (p1_can_play and p2_can_play):
            # proceed as part1
            if p1[0]>p2[0]:
                win, lose = p1, p2
            else:
                win, lose = p2, p1
        else:
            sub1 = [p1[i] for i in range(1,p1[0]+1)]
            sub2 = [p2[i] for i in range(1,p2[0]+1)]
            if part2(sub1, sub2, True):
                win, lose = p1, p2
            else:
                win, lose = p2, p1
        win.append(win.popleft())
        win.append(lose.popleft())
        if (tuple(p1),tuple(p2)) in prior_rounds:
            #print("infinite")
            return True
        prior_rounds.add((tuple(p1),tuple(p2)))

    #print(p1, p2)
    if subgame:
        return len(p1) > len(p2)
    else:
        return score(win)



with open('input22') as fp:
    puzzle = fp.read()

d1,d2 = parse(puzzle.split("\n\n"))
print("#1",play(d1,d2))
print("#2",part2(d1,d2))

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
""".split("\n\n")
d1, d2 = parse(sample)
assert play(d1, d2) == 306

assert part2(d1, d2) == 291

sample_infinite = """\
Player 1:
43
19

Player 2:
2
29
14
""".split("\n\n")
d1, d2 = parse(sample_infinite)
#assert part2(d1,d2)
