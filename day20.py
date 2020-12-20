#!/usr/bin/env python3

def parse(tiles_input):
    def encode(edge):
        edge_bin = ["1" if c == "#" else "0" for c in edge]
        a,b = int(''.join(edge_bin),2), int(''.join(reversed(edge_bin)),2)
        return tuple(sorted([a,b]))

    tiles = dict()  # id : top, right, bottom, left as tuple(low, high)
    for block in tiles_input:
        lines = [line.strip() for line in block.splitlines()]
        header = lines[0]
        assert header.startswith("Tile")
        tile_number = int(header[5:9])
        top = encode(lines[1])
        right = encode("".join([line[-1] for line in lines[1:]]))
        bottom = encode(lines[-1])
        left = encode("".join([line[0] for line in lines[1:]]))
        tiles[tile_number] = (top, right, bottom, left)
    return tiles


def find_edges(tiles):
    """construct a histogram of edges and counts"""
    edges = dict()  # edge : count
    for tile in tiles:
        for edge in tiles[tile]:
            if edge in edges:
                edges[edge] += 1
            else:
                edges[edge] = 1
    return edges
    for edge in edges:
        print(edge,":",edges[edge])

def part1(edges, tiles):
    """ aha!  a corner has 2 edges"""
    result = 1
    for tile in tiles:
        borders = 0
        for edge in tiles[tile]:
            if edges[edge] == 1:
                borders += 1
        if borders > 1:
            #print(tile, "is a corner")
            result *= tile
    return result


with open('input20') as fp:
    input_data = fp.read().split("\n\n")

tiles = parse(input_data)
#print(tiles)
edges = find_edges(tiles)
print("#1",part1(edges, tiles))

sample = """\
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
""".split("\n\n")

tiles = parse(sample)
#print(tiles)
edges = find_edges(tiles)
assert part1(edges, tiles) == 20899048083289
