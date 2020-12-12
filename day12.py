#!/usr/bin/env python3


def part1(lines):
    position = complex(0)  # N,S,E,W = 1j,-1j,1,-1
    heading = complex(1)
    for line in lines:
        go, dist = line[0], int(line[1:])
        if go == "F":
            position += heading * dist
        elif go == "N":
            position += 1j * dist
        elif go == "S":
            position += -1j * dist
        elif go == "W":
            position += -1 * dist
        elif go == "E":
            position += dist
        elif go in "LR":
            if dist == 180:
                heading *= -1
            elif (go == "R" and dist == 90) or (go == "L" and dist == 270):
                heading *= -1j
            elif (go == "L" and dist == 90) or (go == "R" and dist == 270):
                heading *= 1j
            else:
                raise ValueError(f"unexpected rotation {dist}")
        else:
            raise ValueError(f"unexpected direction {go}")
    return int(abs(position.real) + abs(position.imag))


def part2(lines):
    position = complex(0)  # N,S,E,W = 1j,-1j,1,-1
    waypoint = complex(10 + 1j)
    for line in lines:
        go, dist = line[0], int(line[1:])
        if go == "F":
            position += waypoint * dist
        elif go == "N":
            waypoint += 1j * dist
        elif go == "S":
            waypoint += -1j * dist
        elif go == "W":
            waypoint += -1 * dist
        elif go == "E":
            waypoint += dist
        elif go in "LR":
            if dist == 180:
                waypoint *= -1
            elif (go == "R" and dist == 90) or (go == "L" and dist == 270):
                waypoint *= -1j
            elif (go == "L" and dist == 90) or (go == "R" and dist == 270):
                waypoint *= 1j
            else:
                raise ValueError(f"unexpected rotation {dist}")
        else:
            raise ValueError(f"unexpected direction {go}")
    return int(abs(position.real) + abs(position.imag))


with open("input12") as fp:
    input_lines = [line.strip() for line in fp.readlines()]

print("#1", part1(input_lines))
print("#2", part2(input_lines))

sample = """\
F10
N3
F7
R90
F11
""".splitlines()

assert part1(sample) == 25
assert part2(sample) == 286
