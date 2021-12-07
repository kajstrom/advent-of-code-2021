import sys


def sum_diff(crabs, position):
    return sum(map(lambda c: abs(c - position), crabs))


def sum_increasing_diff(crabs, position):
    return sum(map(lambda c: sum(range(1, abs(c - position) + 1)), crabs))


def calculate_cost_to_cheapest(cost_fn, crabs):
    min_crab = min(crabs)
    max_crab = max(crabs)

    cost = sys.maxsize
    for i in range(min_crab, max_crab + 1):
        t_cost = cost_fn(crabs, i)

        if t_cost < cost:
            cost = t_cost

    return cost


with open("inputs/day07.txt") as f:
    crabs = list(map((lambda x: int(x)), f.read().split(",")))

    cost_p1 = calculate_cost_to_cheapest(sum_diff, crabs)
    print(f"Day 07, part 1: {cost_p1}")

    cost_p2 = calculate_cost_to_cheapest(sum_increasing_diff, crabs)
    print(f"Day 07, part 2: {cost_p2}")