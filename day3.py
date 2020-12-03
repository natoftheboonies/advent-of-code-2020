
def parse_mountain(lines):
    mountain = {}
    for y, line in enumerate(lines):
        line = line.strip()
        for x, spot in enumerate(line):
            mountain[(x, y)] = spot

    repeat = len(line)
    vertical_dist = len(lines)
    return mountain, repeat, vertical_dist


def slide(mountain, repeat, vertical_dist, slope=(3,1)):
    x, y = (0, 0)
    trees = 0
    while y < vertical_dist:
        x = (x + slope[0]) % repeat
        y += slope[1]
        if mountain.get((x, y), ".") == "#":
            trees += 1
    return trees


def part2(puzzle):
    result = 1
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees = slide(*puzzle, slope)
        result *= trees
    return result


with open("input3") as fp:
    input_lines = fp.readlines()

puzzle = parse_mountain(input_lines)

print("#1", slide(*puzzle))
print("#2", part2(puzzle))


# sample = """\
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# """.splitlines()

# puzzle = parse_mountain(sample)

# print("#1-sample", slide(*puzzle))
# print("#2-sample", part2(puzzle))
