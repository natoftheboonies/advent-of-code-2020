#!/usr/bin/env python3


class Cup(object):
    """docstring for Cup"""

    def __init__(self, label):
        super(Cup, self).__init__()
        self.label = label
        self.ahead = None

    def insert(self, cup):
        if not cup.ahead:  # add 1
            cup.ahed = self.ahead
        else:  # add 3
            cup.ahead.ahead.ahead = self.ahead
        self.ahead = cup

    def pick3(self):
        first = self.ahead
        third = first.ahead.ahead
        self.ahead = third.ahead
        third.ahead = None
        return first

    def part1(self):
        labels = ""
        search = self.ahead
        while search and search != self:
            labels += str(search.label)
            search = search.ahead
        return labels

    def part2(self):
        return self.ahead.label * self.ahead.ahead.label


def build_ring(puzzle, part2=False):
    cups = []
    cupmap = dict()
    maxcup = 0
    for i in map(int, list(puzzle)):
        cup = Cup(i)
        cupmap[i] = cup
        if i > maxcup:
            maxcup = i
        if cups:
            cups[-1].insert(cup)
        cups.append(cup)
    if part2:
        for i in range(maxcup + 1, 1000000 + 1):
            cup = Cup(i)
            cupmap[i] = cup
            if cups:
                cups[-1].insert(cup)
            cups.append(cup)
        maxcup = i
    # complete the circle
    cup.ahead = cups[0]
    assert len(cupmap.keys()) == maxcup

    return cups, cupmap, maxcup


def determine_destination(current, pick3, maxcup):
    destination = current.label - 1
    while destination in (pick3.label, pick3.ahead.label, pick3.ahead.ahead.label):
        destination -= 1
    if destination < 1:
        destination = maxcup
        while destination in (pick3.label, pick3.ahead.label, pick3.ahead.ahead.label):
            destination -= 1
    return destination


def part1(puzzle, moves):
    cups, cupmap, maxcup = build_ring(puzzle)
    current = cups[0]
    for _ in range(moves):
        pick3 = current.pick3()
        destination = determine_destination(current, pick3, maxcup)
        cupmap[destination].insert(pick3)
        current = current.ahead
    return cupmap[1].part1()


def part2(puzzle):
    cups, cupmap, maxcup = build_ring(puzzle, True)
    current = cups[0]
    for x in range(10000000):
        pick3 = current.pick3()
        destination = determine_destination(current, pick3, maxcup)
        cupmap[destination].insert(pick3)
        current = current.ahead
    return cupmap[1].part2()


puzzle = "193467258"
print("#1", part1(puzzle, 100))
print("#2", part2(puzzle))

sample = "389125467"
assert part1(sample, 10) == "92658374"
assert part1(sample, 100) == "67384529"
# assert part2(sample)==149245887792
