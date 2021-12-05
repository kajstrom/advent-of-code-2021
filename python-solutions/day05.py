from functools import reduce
from operator import iconcat
from copy import deepcopy


def parse_coords(coords):
    start, to = coords
    s_x, s_y = start.split(",")
    s_x = int(s_x)
    s_y = int(s_y)

    t_x, t_y = to.split(",")
    t_x = int(t_x)
    t_y = int(t_y)

    return [(s_x, s_y), (t_x, t_y)]

def read_input():
    with open("inputs/day05.txt") as f:
        lines = f.read().splitlines()
        lines = map(lambda l: l.split(" -> "), lines)
        coords = map(parse_coords, lines)

        return list(coords)


coords = read_input()


def make_coord_range(coord, diff):
    values = []
    if diff < 0:
        for x in range(coord, coord - abs(diff) - 1, -1):
            values.append(x)
    elif diff > 0:
        for x in range(coord, coord + diff + 1):
            values.append(x)

    return values


def expand_line(line):
    start, end = line

    x_diff = end[0] - start[0]
    y_diff = end[1] - start[1]

    expanded_line = []

    if x_diff != 0 and y_diff != 0:
        x_range = make_coord_range(start[0], x_diff)
        y_range = make_coord_range(start[1], y_diff)

        for x, y in zip(x_range, y_range):
            expanded_line.append((x, y))

    elif x_diff != 0:
        for x in make_coord_range(start[0], x_diff):
            expanded_line.append((x, start[1]))
    elif y_diff != 0:
        for y in make_coord_range(start[1], y_diff):
            expanded_line.append((start[0], y))

    return expanded_line


def calculate_overlaps(coords):
    expanded_coords = list(map(expand_line, coords))
    flat_expanded_coords = list(reduce(iconcat, deepcopy(expanded_coords)))

    results = {}

    for coord in flat_expanded_coords:
        if coord in results:
            results[coord] += 1
        else:
            results[coord] = 1

    two_plus_overlaps = list(filter(lambda x: x >= 2, results.values()))
    return len(two_plus_overlaps)


def part1():
    hor_ver_coords = list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], coords))
    print(f"Day 5, part 1: {calculate_overlaps(hor_ver_coords)}")


def part2():
    print(f"Day 5, part 2: {calculate_overlaps(coords)}")


part1()
part2()
