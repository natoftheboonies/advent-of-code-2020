#!/usr/bin/env python3

import math


def encode(edge):
    edge_bin = ["1" if c == "#" else "0" for c in edge]
    a, b = int("".join(edge_bin), 2), int("".join(reversed(edge_bin)), 2)
    return tuple(sorted([a, b]))


class Tile(object):
    """docstring for Tile"""

    def __init__(self, number, lines):
        super(Tile, self).__init__()
        self.number = number
        self.lines = lines

    def left(self):
        return "".join([line[0] for line in self.lines])

    def left_enc(self):
        return encode(self.left())

    def right(self):
        return "".join([line[-1] for line in self.lines])

    def right_enc(self):
        return encode(self.right())

    def top(self):
        return self.lines[0]

    def top_enc(self):
        return encode(self.top())

    def bottom(self):
        return self.lines[-1]

    def bottom_enc(self):
        return encode(self.bottom())

    def edges_enc(self):
        return (self.top_enc(), self.right_enc(), self.bottom_enc(), self.left_enc())

    def image_lines(self):
        return [line[1:-1] for line in self.lines[1:-1]]

    def rotate_c(self):  # clockwise
        self.lines = ["".join(line) for line in list(zip(*self.lines[::-1]))]

    def mirror_v(self):  # vertical
        self.lines = self.lines[::-1]

    def mirror_h(self):  # horizontal
        self.lines = [line[::-1] for line in self.lines]

    def orient(self, edges, neighbors):
        # match orientation to left/top tiles
        if any(isinstance(n, Tile) for n in neighbors):
            if isinstance(neighbors[0], Tile):
                # top neighbor
                neighbor = neighbors[0]
                while self.top_enc() != neighbor.bottom_enc():
                    self.rotate_c()
                if self.top() != neighbor.bottom():
                    self.mirror_h()
            # filling l->r, t->b so don't need to check right or bottom
            if isinstance(neighbors[3], Tile):
                # left neighbor
                neighbor = neighbors[3]
                while self.left_enc() != neighbor.right_enc():
                    self.rotate_c()
                if self.left() != neighbor.right():
                    self.mirror_v()
        elif 0 in neighbors:  # orient to outer border
            target = tuple((1 if e == 0 else 2 for e in neighbors))
            while tuple(edges[edge] for edge in self.edges_enc()) != target:
                current = tuple(edges[edge] for edge in self.edges_enc())
                self.rotate_c()

        # check ourselves
        if neighbors[0] is not None:
            if neighbors[0] == 0:
                assert edges[self.top_enc()] == 1
            else:
                assert self.top() == neighbors[0].bottom()

        if neighbors[3] is not None:
            if neighbors[3] == 0:
                assert edges[self.left_enc()] == 1
            else:
                assert self.left() == neighbors[3].right()

    def __repr__(self):
        return "Tile: " + str(self.number)


def parse(tiles_input):
    tiles = []
    for block in tiles_input:
        lines = [line.strip() for line in block.splitlines()]
        header = lines[0]
        assert header.startswith("Tile")
        tile_number = int(header[5:9])
        tile = Tile(tile_number, lines[1:])
        tiles.append(tile)
    return tiles


def find_edges(tiles):
    """construct a histogram of edges and counts"""
    edges = dict()  # edge : count
    for tile in tiles:
        for edge in tile.edges_enc():
            if edge in edges:
                edges[edge] += 1
            else:
                edges[edge] = 1
    return edges


def find_corners(tiles, edges):
    """ aha!  a corner has 2 edges"""
    corners = []
    for tile in tiles:
        borders = 0
        for edge in tile.edges_enc():
            if edges[edge] == 1:
                borders += 1
        if borders > 1:
            corners.append(tile)
    return corners


def part1(tiles, edges):
    result = 1
    for tile in find_corners(tiles, edges):
        result *= tile.number
    return result


monster_img = """\
                  #
#    ##    ##    ###
 #  #  #  #  #  #
""".splitlines()

monster = list()
for y, line in enumerate(monster_img):
    for x, c in enumerate(line):
        if c == "#":
            monster.append((x, y))

monster_max_y = max((y for x, y in monster))
monster_max_x = max((x for x, y in monster))


def find_monsters(image):
    # assume no overlapping monsters
    monsters = 0
    for y in range(len(image) - monster_max_y):
        for x in range(len(image[y]) - monster_max_x):
            if all(image[y + dy][x + dx] == "#" for dx, dy in monster):
                # print("found a monster!")
                monsters += 1
    if monsters > 0:
        roughness = sum(line.count("#") for line in image)
        return roughness - monsters * len(monster)
    return None


def solve_puzzle(tiles, edges):
    puzzle_edge = math.isqrt(len(tiles))
    puzzle = [[None] * puzzle_edge for _ in range(puzzle_edge)]

    # fill in the puzzle
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            top = puzzle[y - 1][x] if y > 0 else 0
            right = puzzle[y][x + 1] if x < len(puzzle[y]) - 1 else 0
            bottom = puzzle[y + 1][x] if y < len(puzzle) - 1 else 0
            left = puzzle[y][x - 1] if x > 0 else 0
            if x == y == 0:
                # place a corner in top-left
                match = find_corners(tiles, edges)[0]
                match.mirror_h()
            elif 0 < x < len(puzzle[y]):  # find piece matching neighbor left
                match = [tile for tile in tiles if tile != left and left.right_enc() in tile.edges_enc()][0]
            elif 0 < y < len(puzzle):  # find piece matching neighbor top
                match = [tile for tile in tiles if tile != top and top.bottom_enc() in tile.edges_enc()][0]
            # place it
            puzzle[y][x] = match
            # orient it
            match.orient(edges, (top, right, bottom, left))

    # now let's join it
    piece_lines = len(puzzle[0][0].image_lines())
    image_size = puzzle_edge * piece_lines

    image = [""] * image_size

    for line in range(image_size):
        y = line // piece_lines
        for x in range(len(puzzle[0])):
            piece = puzzle[y][x]
            image[line] += piece.image_lines()[line % piece_lines]

    # check permutations of image
    for _ in range(3):
        result = find_monsters(image)
        if result:
            return result
        image = ["".join(line) for line in list(zip(*image[::-1]))]
    image = [line[::-1] for line in image]
    for _ in range(3):
        result = find_monsters(image)
        if result:
            return result
        image = ["".join(line) for line in list(zip(*image[::-1]))]


def part2(tiles, edges):
    return solve_puzzle(tiles, edges)


with open("input20") as fp:
    input_data = fp.read().split("\n\n")

tiles = parse(input_data)
edges = find_edges(tiles)
print("#1", part1(tiles, edges))
print("#2", part2(tiles, edges))


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
""".split(
    "\n\n"
)

tiles = parse(sample)
edges = find_edges(tiles)

assert part1(tiles, edges) == 20899048083289
assert part2(tiles, edges) == 273
