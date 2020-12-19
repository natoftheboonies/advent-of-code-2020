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

    def check42(message):
        #print("checking",message)
        if len(message)<5:
            return True
        for r in resolved[42]:
            if message==r:
                return True
            elif message.startswith(r):
                return check42(message[len(r):])
        return False

    messages = set((m.strip() for m in message_lines))
    #print("messages", len(messages))

    rules = parse(rule_lines)
    rules[8]=[(42,),(42,8)]  # (42)+
    rules[11]=[(42,31),(42,11,31)]  # (42){n}(31){n} for some n>0
    rules[0]=[(8,11)]  # (42)+(42){n}(31){n}
    count = 0

    resolved = dict()
    for x in rules:
        if x in (0,8,11):
            continue
        resolved[x] = generate(rules,x)
        # if x in (42,31):
        #     print(resolved[x])


    # for e in resolved[42]:
    #     break
    # size = len(e)
    # print("42s are",size)
    # print("and we have",len(resolved[42]),"out of",2**size)
    # for e in resolved[31]:
    #     break
    # size = len(e)
    # print("31s are",size)
    # print("and we have",len(resolved[31]),"out of",2**size)

    regex42 = ["("]
    for x in resolved[42]:
        regex42.append(x)
        regex42.append("|")
    regex42[-1] = ")"
    regex42 = ''.join(regex42)

    regex31 = ["("]
    for x in resolved[31]:
        regex31.append(x)
        regex31.append("|")
    regex31[-1] = ")"
    regex31 = ''.join(regex31)

    # ((42)(42))+(31)+
    #bigolregex = r"^("+regex42+regex42+")+"+regex31+"+$"
    p10 = []
    # (42)+(42){n}(31){n}
    for loop in range(1,12):
        thisregex = r"^"+regex42+"+"
        thisregex+=regex42+"{"+str(loop)+"}"
        thisregex+=regex31+"{"+str(loop)+"}"
        thisregex += "$"
        p10.append(re.compile(thisregex))

    #bigolregex = r"^"+regex42+"+"+regex42+"{n}"+regex31+"{n}$"
    #p = re.compile(bigolregex)

    for m in messages:
        #print("checking",m)
        if any((p.match(m) for p in p10)):
            #print(m,"matched it")
            count+=1

    #print("rules",rules)
    return count


with open('input19') as fp:
    rulepart, checkpart = fp.read().split("\n\n")

print("#1",part1(rulepart.splitlines(),checkpart.splitlines()))
print("#2",part2(rulepart.splitlines(),checkpart.splitlines()))

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