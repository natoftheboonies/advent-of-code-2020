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

rules = parse(sample[0].splitlines())
options = generate(rules,0)
print(options)
count = 0
for x in sample[1].splitlines():
    print(x)
    if x in options:
        count+=1
print(count)
#print(sample[1])

with open('input19') as fp:
    rulepart, checkpart = fp.read().split("\n\n")

rules = parse(rulepart.splitlines())
print(len(rules))
big = generate(rules,0)
count = 0
for x in checkpart.splitlines():
    if x.strip() in big:
        count += 1
print("#1",count)