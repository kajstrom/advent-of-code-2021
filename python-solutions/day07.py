import sys


def read_input():
    with open("inputs/day07.txt") as f:
        return list(map((lambda x: int(x)), f.read().split(",")))


def part1():
    crabs = read_input()

    min_crab = min(crabs)
    max_crab = max(crabs)

    cost = sys.maxsize
    for i in range(min_crab, max_crab + 1):
        t_cost = sum(map(lambda c: abs(c - i), crabs))

        if t_cost < cost:
            cost = t_cost

    print(f"Day 07, part 1: {cost}")


def part2():
    crabs = read_input()

    min_crab = min(crabs)
    max_crab = max(crabs)

    cost = sys.maxsize
    for i in range(min_crab, max_crab + 1):
        t_cost = sum(map(lambda c: sum(range(1, abs(c - i) + 1)), crabs))

        if t_cost < cost:
            cost = t_cost

    print(f"Day 07, part 2: {cost}")


part1()
part2()
