#!/usr/bin/env python3


def seatnum(bpass):
    bin_row = "".join(["1" if c == "B" else "0" for c in bpass[:7]])
    bin_col = "".join(["1" if c == "R" else "0" for c in bpass[7:]])
    return int(bin_row, 2) * 8 + int(bin_col, 2)


with open("input5") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

seats = [seatnum(x) for x in input_lines]

print("#1", max(seats))
print("#2", [seat for seat in range(min(seats), max(seats) + 1) if seat not in seats][0])


# 00101100
#  FBFBBFF
assert seatnum("FBFBBFFRLR") == 357
assert seatnum("BFFFBBFRRR") == 567
assert seatnum("BBFFBBFRLL") == 820
