#!/usr/bin/env python3


def parse(lines):
    combos = []
    for line in lines:
        left, right = line[:-1].split(" (contains ")
        ingredients = set(left.split())
        allergins = set(r.strip(",") for r in right.split())
        combos.append((ingredients, allergins))
    return combos


def solve(combos):
    possible = dict()
    for ingredients, allergins in combos:
        for allergin in allergins:
            if allergin in possible:
                possible[allergin] = possible[allergin].intersection(ingredients)
            else:
                possible[allergin] = ingredients
    while any(isinstance(p, set) for p in possible.values()):
        for p in possible:
            if len(possible[p]) == 1:
                possible[p] = list(possible[p])[0]
                for p2 in possible:
                    if isinstance(possible[p2], set):
                        possible[p2].discard(possible[p])

    dangerous = ",".join(possible[k] for k in sorted(possible.keys()))

    safe = 0
    for ingredients, allergins in combos:
        for ingredient in ingredients:
            if not any(ingredient in unsafe for unsafe in possible.values()):
                # print(ingredient,"is safe")
                safe += 1
    return safe, dangerous


with open("input21") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

safe, dangerous = solve(parse(input_lines))
print("#1", safe)
print("#2", dangerous)

sample = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".splitlines()

safe, dangerous = solve(parse(sample))
assert safe == 5
assert dangerous == "mxmxvkd,sqjhc,fvjkl"
