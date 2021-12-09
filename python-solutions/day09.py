def read_input():
    with open("inputs/day09.txt") as f:
        return list(map(lambda r: list(map(int, list(r))), f.read().splitlines()))


lava_tubes = read_input()


def collect_adjacent(lava_tubes, x, y) -> list[int]:
    max_x = len(lava_tubes) - 1
    max_y = len(lava_tubes[0]) -1

    adjacent = []

    #top
    if x - 1 >= 0:
        adjacent.append(lava_tubes[x - 1][y])

    #bottom
    if x + 1 <= max_x:
        adjacent.append(lava_tubes[x + 1][y])

    #left
    if y - 1 >= 0:
        adjacent.append(lava_tubes[x][y - 1])

    #right
    if y + 1 <= max_y:
        adjacent.append(lava_tubes[x][y + 1])

    return adjacent


def is_low_point(adjacent, current) -> bool:
    for lava_tube in adjacent:
        if current >= lava_tube:
            return False

    return True


def part1():
    low_points = []

    for x in range(0, len(lava_tubes)):
        for y in range(0, len(lava_tubes[x])):
            current = lava_tubes[x][y]
            adjacent = collect_adjacent(lava_tubes, x, y)

            if is_low_point(adjacent, current):
                low_points.append(current)

    print(low_points)
    risk_level = sum(map(lambda l: l + 1, low_points))
    print(f"Day 09, part 1: {risk_level}")


part1()
