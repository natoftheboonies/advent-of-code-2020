#!/usr/bin/env python3


class Cup(object):
    """docstring for Cup"""
    def __init__(self, label):
        super(Cup, self).__init__()
        self.label = label
        self.ahead = None

    def insert(self, cup):
        cup.findend().ahead = self.ahead
        self.ahead = cup


    def pick3(self):
        first = self.ahead
        second = first.ahead
        third = second.ahead
        self.ahead = third.ahead
        third.ahead = None
        return first

    def findend(self):
        search = self.ahead
        count = 0
        if not search:
            return self
        else:
            while search.ahead and search != self:
                count += 1
                search = search.ahead
            assert count < 3
            return search



    def tolist(self):
        labels = [self.label]
        search = self.ahead
        while search and search != self:
            labels.append(search.label)
            search = search.ahead
        return labels

    def findcup(self,label):
        if self.label == label:
            return self
        search = self.ahead
        while search and search != self:
            if search.label == label:
                return search
            search = search.ahead
        return None


    def __str__(self):
        if self.ahead:
            return str(self.label)+"->"+str(self.ahead.label)
        else:
            return str(self.label)+"->None"

def build_ring(puzzle):
    cups = []
    for i in puzzle:
        cup = Cup(int(i))
        if cups:
            cups[-1].insert(cup)
        cups.append(cup)
    # complete the circle
    cups[-1].ahead = cups[0]
    return cups


def part1(puzzle, moves):
    cups = build_ring(puzzle)

    current = cups[0]
    cupmap = {current.label: current}
    ahead = current.ahead
    while ahead != current:
        cupmap[ahead.label] = ahead
        ahead = ahead.ahead
    maxcup = 9
    assert len(cupmap.keys())==maxcup

    for _ in range(moves):
        pick3 = current.pick3()
        destination = current.label - 1
        while destination in (pick3.label, pick3.ahead.label, pick3.ahead.ahead.label):
            destination -= 1
        if destination < 1:
            destination = maxcup
            while destination in (pick3.label, pick3.ahead.label, pick3.ahead.ahead.label):
                destination -= 1
        # for target in range(current.label-1, current.label-4,-1):
        #     if target < 1 or pick3.findcup(target) is not None:
        #         continue
        #     destination = target
        #     break
        # if not destination:
        #     for target in range(maxcup, maxcup-4,-1):
        #         if not pick3.findcup(target) is not None:
        #             destination = target
        #             break
        cupmap[destination].insert(pick3)
        # move ahead
        current = current.ahead
    return ''.join(str(i) for i in cupmap[1].tolist()[1:])


def part2(puzzle):
    cupmap = dict()
    labels = list(puzzle)
    firstcup = None
    lastcup = None
    for i in labels:
        cup = Cup(int(i))
        cupmap[cup.label] = cup
        if not lastcup:
            firstcup = cup
        else:
            lastcup.insert(cup)
        lastcup = cup
    maxcup = 1000000
    for i in range(10,maxcup+1):
        cup = Cup(i)
        cupmap[cup.label] = cup
        lastcup.insert(cup)
        lastcup = cup
    lastcup.ahead = firstcup
    current = firstcup
    # print("first",firstcup)
    # print("last",lastcup)
    assert len(cupmap.keys())==maxcup
    for x in range(10000000):
        pick3 = current.pick3()
        destination = current.label - 1
        while destination in (pick3.label, pick3.ahead.label, pick3.ahead.ahead.label):
            destination -= 1
        if destination < 1:
            destination = maxcup
            while destination in (pick3.label, pick3.ahead.label, pick3.ahead.ahead.label):
                destination -= 1
            # for target in range(maxcup, maxcup-3,-1):
            #     if not pick3.findcup(target):
            #         destination = target
            #         break
        #print("dest",destination,"for current",current.label)
        cupmap[destination].insert(pick3)
        # move ahead
        current = current.ahead
    cup1 = cupmap[1]
    #print("1 seq", cup1, cup1.ahead, cup1.ahead.ahead)
    return cup1.ahead.label*cup1.ahead.ahead.label

puzzle = "193467258"
print("#1",part1(puzzle,100))
print("#2",part2(puzzle)) # 744529654 too low, 602154808356 too high

sample = "389125467"
assert part1(sample,10)=="92658374"
assert part1(sample,100)=="67384529"
#assert part2(sample)==149245887792

