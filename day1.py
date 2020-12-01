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

numbers = list(sorted(map(int,[line.strip() for line in lines])))


def part1(numbers):
	for x in numbers:
		for y in numbers:
			if x+y==2020:
				return x*y

def part1faster(number):
	for i in range(len(numbers)):
		for j in range(i+1, len(numbers)):
				if numbers[i]+numbers[j]==2020:
					return numbers[i]*numbers[j]

def part2(numbers):
	for x in numbers:
		for y in numbers:
			for z in numbers:
				if x+y+z==2020:
					return x*y*z

def part2faster(number):
	for i in range(len(numbers)):
		for j in range(i+1, len(numbers)):
			if numbers[i]+numbers[j] >= 2020:
				continue
			for k in range(j+1, len(numbers)):
				if numbers[i]+numbers[j]+numbers[k]==2020:
					return numbers[i]*numbers[j]*numbers[k]

print("#1", part1faster(numbers))
print("#1", part2faster(numbers))