#!/usr/bin/env python3


def seatnum(bpass):
    bin_seat = "".join(["1" if c in "BR" else "0" for c in bpass])
    return int(bin_seat, 2)


with open("input5") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

seats = [seatnum(x) for x in input_lines]

print("#1", max(seats))
print("#2", [seat for seat in range(min(seats), max(seats) + 1) if seat not in seats][0])

# https://math.stackexchange.com/questions/2713656/how-to-calculate-sum-of-the-integers-from-m-to-n
# via https://www.reddit.com/r/adventofcode/comments/k71h6r/2020_day_05_solutions/gepe8a5/
# s = int(((min(seats) + max(seats)) * (max(seats) - min(seats) + 1)) / 2)
# print(s - sum(seats))


# 00101100
#  FBFBBFF
assert seatnum("FBFBBFFRLR") == 357
assert seatnum("BFFFBBFRRR") == 567
assert seatnum("BBFFBBFRLL") == 820
