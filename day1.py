#!/usr/bin/env python3

# day1

with open('input1') as fp:
	lines = [line.strip() for line in fp.readlines()]

sample = """\
1721
979
366
299
675
1456
""".splitlines()

numbers = list(map(int,[line.strip() for line in lines]))


def part1(numbers):
	for x in numbers:
		for y in numbers:
			if x+y==2020:
				return x*y

def part2(numbers):
	for x in numbers:
		for y in numbers:
			for z in numbers:
				if x+y+z==2020:
					return x*y*z


print("#1", part1(numbers))
print("#1", part2(numbers))