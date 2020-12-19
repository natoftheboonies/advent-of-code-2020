#!/usr/bin/env python3


def parse(lines):
    rules = dict()
    for line in lines:
        k, v = line.split(":")
        rules[int(k)] = v
        # a or [(4,1,5)] or [(2,3),(3,2)]
        if '"' in v:
            rules[int(k)] = v.strip(' "\n')
        elif '|' in v:
            rules[int(k)] = [tuple(map(int,option.strip().split())) for option in v.split("|")]
        else:
            rules[int(k)] = [tuple(map(int,v.strip().split()))]
    return rules


from itertools import product

def generate(rules,cur):
    matches = set()
    rule = rules[cur]
    if not isinstance(rule,list):
        return rule
    else:
        #print("rule",rule)
        for case in rule:
            #print("case",case)
            results = []
            for r in case:
                tails = generate(rules,r)
                results.append(tails)
                #print(r,"yielded",tails)
            #print("results",results)
            for x in product(*results):
                #print("product",x)
                matches.add(''.join(x))
    return matches


def part1(rule_lines, message_lines):
    rules = parse(rule_lines)
    #print(len(rules))
    big = generate(rules,0)
    count = 0
    for x in message_lines:
        if x.strip() in big:
            count += 1
    return count

import re

def part2(rule_lines, message_lines):

    messages = set((m.strip() for m in message_lines))
    print("messages", len(messages))

    for i, r in enumerate(rule_lines):
        if r.startswith("8: "):
            rule_lines[i] = '8: "x"'
        elif r.startswith("11: "):
            rule_lines[i] = '11: "y"'

    rules = parse(rule_lines)

    print("rules",rules)
    print("42",generate(rules,42))
    print("31",generate(rules,31))
    print(big)
    #print(rules[0])

    count = 0

    # 11 = 42 31 | 42 11 31
    # =
    rule42 = generate(rules,42)
    rule31 = generate(rules,31)
    print("42",rule42)
    print("31",rule31)
    # how many contain a 31*42 ?
    both4231 = [c for c in product(rule42,rule31)]
    print('both',len(both4231))
    for b in both4231:
        nonregx = ''.join(b)
        regex = r'('+b[0]+r')+('+b[1]+r')+'
        p = re.compile(regex)
        #print(p)
        candidates = set()
        for m in messages:
            if p.search(m):
                candidates.add(m)
        if candidates:
            print("rule",regex,"matched",len(candidates))
    print(candidates)
    # how many contain an 8?
    for rule in rule8:
        regex = "^("+rule+")+$"
        p = re.compile(regex)
        matched = set()
        for m in messages:
            if p.search(m):
                matched.add(m)
        if matched:
            print("rule",regex,"matched",len(matched))
    messages -= matched
    #print("rule",rules[8])
    #print(len(rules))
    big = generate(rules,0)

    for x in messages:
        if x.strip() in big:
            count += 1
    print("count",count)
    return count


with open('input19') as fp:
    rulepart, checkpart = fp.read().split("\n\n")

#print("#1",part1(rulepart.splitlines(),checkpart.splitlines()))
#print("#2",part2(rulepart.splitlines(),checkpart.splitlines()))

sample = """\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".split("\n\n")

sample_rule_lines = sample[0].splitlines()
sample_message_lines = sample[1].splitlines()
assert part1(sample_rule_lines,sample_message_lines)==2

sample2 = """\
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""".split("\n\n")

sample2_rule_lines = sample2[0].splitlines()
sample2_message_lines = sample2[1].splitlines()
assert part1(sample2_rule_lines,sample2_message_lines)==3
assert part2(sample2_rule_lines,sample2_message_lines)==12