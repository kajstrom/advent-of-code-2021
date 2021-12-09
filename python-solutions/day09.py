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

    risk_level = sum(map(lambda l: l + 1, low_points))
    print(f"Day 09, part 1: {risk_level}")


def collect_adjacent_coords(lava_tubes, loc, visited = None) -> list[tuple[int, int]]:
    x, y = loc
    max_x = len(lava_tubes) - 1
    max_y = len(lava_tubes[0]) -1

    adjacent = []

    #top
    if x - 1 >= 0:
        adjacent.append((x - 1, y))

    #bottom
    if x + 1 <= max_x:
        adjacent.append((x + 1, y))

    #left
    if y - 1 >= 0:
        adjacent.append((x, y - 1))

    #right
    if y + 1 <= max_y:
        adjacent.append((x, y + 1))

    if visited is not None:
        unvisited_adjacent = []
        for loc in adjacent:
            if loc not in visited:
                unvisited_adjacent.append(loc)

        return unvisited_adjacent

    return adjacent


def get_value(lava_tubes, loc) -> int:
    x, y = loc
    return lava_tubes[x][y]


def part2():
    low_points = []

    for x in range(0, len(lava_tubes)):
        for y in range(0, len(lava_tubes[x])):
            current = lava_tubes[x][y]
            adjacent = collect_adjacent(lava_tubes, x, y)

            if is_low_point(adjacent, current):
                low_points.append((x, y))

    basins = []
    for low_point in low_points:
        visited = [low_point]
        to_visit = collect_adjacent_coords(lava_tubes, low_point)

        for visit in to_visit:
            visit_value = get_value(lava_tubes, visit)

            if visit_value == 9:
                continue

            adjacent = collect_adjacent_coords(lava_tubes, visit, visited)

            for loc in adjacent:
                if loc not in to_visit:
                    to_visit.append(loc)

            visited.append(visit)

        basins.append(visited)

    basins_by_len = sorted(basins, key=len, reverse=True)

    basin_sizes = list(map(len, basins_by_len))
    first, second, third = basin_sizes[:3]
    print(f"Day 09, part 2: {first * second * third}")


part1()
part2()
