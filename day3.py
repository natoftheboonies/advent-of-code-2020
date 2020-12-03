
SLOPE = (3,1)

def parse_mountain(lines):
	mountain = {}
	for y, line in enumerate(lines):
		line = line.strip()
		for x, spot in enumerate(line):
			mountain[(x,y)]=spot

	repeat = len(line)
	vertical_dist = len(lines)
	return mountain, repeat, vertical_dist


def slide(lines, slope=SLOPE):
	mountain, repeat, vertical_dist	= parse_mountain(lines)
	x,y=(0,0)
	trees = 0
	while y < vertical_dist:
		x = (x+slope[0])%repeat
		y+=slope[1]
		if mountain.get((x,y),'.')=='#':
			trees += 1
	return trees


def part2(lines):
	result = 1
	for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
		slid = slide(lines,slope)
		print(slope, slid)
		result *= slid
	return result

with open('input3') as fp:
	input_lines = fp.readlines()


print("#1",slide(input_lines))
print("#2",part2(input_lines))


sample = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".splitlines()


print("#1-sample",slide(sample))

print("#2-sample",part2(sample))

