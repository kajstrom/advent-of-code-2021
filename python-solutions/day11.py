from utils import get_coords, set_coords


def read_input(file):
    with open(file) as f:
        return list(map(lambda r: list(map(int, list(r))), f.read().splitlines()))


def adjacent_coords(octopuses, coord):
    x, y = coord
    max_x = len(octopuses)
    max_y = len(octopuses[0])

    adjacent = []
    for c_x in range(x - 1, x + 2):
        for c_y in range(y - 1, y + 2):
            if c_x >= 0 and c_x < max_x and c_y >= 0 and c_y < max_y:
                adj_coord = (c_x, c_y)

                if adj_coord != coord:
                    adjacent.append(adj_coord)

    return adjacent


def flash_spill(octopuses, adjacent):
    further_adjacent = []
    flashes = 0
    for coord in adjacent:
        value = get_coords(octopuses, coord)
        if value != 0:
            set_coords(octopuses, coord, value + 1)

        if get_coords(octopuses, coord) > 9:
            set_coords(octopuses, coord, 0)
            flashes += flash(octopuses, coord)

    return further_adjacent, flashes


def flash(octopuses, coord):
    x, y = coord
    # collect adjacent
    adjacent = adjacent_coords(octopuses, (x, y))
    octopuses[x][y] = 0
    total_flashes = 1

    while len(adjacent) > 0:
        adjacent, flashes = flash_spill(octopuses, adjacent)
        total_flashes += flashes

    return total_flashes


def visualize(octopuses):
    for row in octopuses:
        print(row)


def part1():
    octopuses = read_input("inputs/day11.txt")

    total_flashes = 0
    for step in range(1, 101):
        # increase energy level
        for x in range(0, len(octopuses)):
            for y in range(0, len(octopuses[x])):
                octopuses[x][y] += 1

        # flash
        for x in range(0, len(octopuses)):
            for y in range(0, len(octopuses[x])):
                octopus = octopuses[x][y]
                if octopus > 9:
                    total_flashes += flash(octopuses, (x, y))

    print(f"Day 11, part 1: {total_flashes}")



if __name__ == '__main__':
    part1()