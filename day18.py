#!/usr/bin/env python3

import re


def newmath(expr):
    result = None
    e = expr.split()
    result = int(e[0])
    for i in e[1:]:
        if not i.isnumeric():
            op = i
        else:
            result = eval(str(result)+op+i)
    return result

assert newmath("1 + 2 * 3 + 4 * 5 + 6") == 71

def plusfirst(expr):
    matches = list(re.finditer(r"(\d+ \+ \d+)", expr))
    while matches:
        for match in reversed(matches):
            #print(match, "=", newmath(match.group(0)))
            expr = expr[:match.start()]+str(newmath(match.group(0)))+expr[match.end():]
            #print(".",expr)
        matches = list(re.finditer(r"(\d+ \+ \d+)", expr))

    assert '+' not in expr
    return newmath(expr)

def part1(expr,part2=False):
    matches = re.findall(r"(\([^()]+\))", expr)
    while matches:
        for match in matches:
            #print(match, "=", newmath(match[1:-1]))
            if part2:
                expr = expr.replace(match,str(plusfirst(match[1:-1])))
            else:
                expr = expr.replace(match,str(newmath(match[1:-1])))
        matches = re.findall(r"(\([^()]+\))", expr)
    if part2:
        return plusfirst(expr)
    else:
        return newmath(expr)

assert part1("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert part1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")==12240

with open('input18') as fp:
    lines = [line.strip() for line in fp.readlines()]

result = sum(part1(line) for line in lines)
print("#1",result)

assert part1("1 + 2 * 3 + 4 * 5 + 6",True)==231
assert part1("1 + (2 * 3) + (4 * (5 + 6))",True)==51
assert part1("2 * 3 + (4 * 5)",True)==46
assert part1("5 + (8 * 3 + 9 + 3 * 4 * 3)",True)==1445
assert part1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",True)==669060
assert part1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",True)==23340


print("#2",sum(part1(line,True) for line in lines)) # not 535809599856883
