#!/usr/bin/env python3


def reduce_moves(moves):
    """ from 2017 day 11 :) """
    if "sw" in moves and "ne" in moves:
        if moves["sw"] > moves["ne"]:
            moves["sw"] -= moves["ne"]
            moves.pop("ne")
        else:
            moves["ne"] -= moves["sw"]
            moves.pop("sw")
    if "nw" in moves and "se" in moves:
        if moves["nw"] > moves["se"]:
            moves["nw"] -= moves["se"]
            moves.pop("se")
        else:
            moves["se"] -= moves["nw"]
            moves.pop("nw")
    if "e" in moves and "w" in moves:
        if moves["e"] > moves["w"]:
            moves["e"] -= moves["w"]
            moves.pop("w")
        else:
            moves["w"] -= moves["e"]
            moves.pop("e")
    return moves


def follow(moves):
    x = y = 0
    for d in moves:

        if d == "e":
            x += moves[d] * 2
        elif d == "w":
            x -= moves[d] * 2
        elif "e" in d:
            x += moves[d]
            if "s" in d:
                y -= moves[d]
            elif "n" in d:
                y += moves[d]
        elif "w" in d:
            x -= moves[d]
            if "s" in d:
                y -= moves[d]
            elif "n" in d:
                y += moves[d]
    return x, y


def parse(lines):
    paths = []
    for line in lines:
        c = 0
        moves = {}
        while c < len(line.strip()):
            if line[c] in ("s", "n"):
                move = line[c : c + 2]
                c += 2
            else:
                move = line[c]
                c += 1
            if move in moves:
                moves[move] += 1
            else:
                moves[move] = 1
        moves = reduce_moves(moves)
        result = follow(moves)
        paths.append(result)
    return paths


def flip(paths):
    tiles = set()
    for tile in paths:
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.add(tile)
    return tiles


def part1(paths):
    return len(flip(paths))


hex_neighbors = ((1, 1), (-1, -1), (1, -1), (-1, 1), (2, 0), (-2, 0))


def part2(paths):
    state = flip(paths)
    for _ in range(100):
        state_n = set()
        neighbors = set()
        for pos in state:
            x, y = pos
            # check pos for 0 or >2 neighbors
            count = 0
            for dx, dy in hex_neighbors:
                neighbor = (x + dx, y + dy)
                neighbors.add(neighbor)
                if neighbor in state:
                    count += 1
            if 0 < count <= 2:
                state_n.add(pos)
        for pos in neighbors:
            if pos in state:
                continue
            x, y = pos
            count = 0
            for dx, dy in hex_neighbors:
                neighbor = (x + dx, y + dy)
                if neighbor in state:
                    count += 1
            if count == 2:
                state_n.add(pos)
        state = state_n
        # print("next: ",len(state))
    return len(state)


with open("input24") as fp:
    lines = [line.strip() for line in fp.readlines()]

paths = parse(lines)
print("#1", part1(paths))
print("#2", part2(paths))

sample = """\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
""".splitlines()

paths = parse(sample)
assert part1(paths) == 10
assert part2(paths) == 2208
