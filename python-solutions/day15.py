import sys
from functools import reduce

def read_input(file):
    with open(file) as f:
        return list(map(lambda l: list(map(int, list(l))), f.read().splitlines()))


class Node:
    def __init__(self, coords, risk):
        self.coords = coords
        self.risk = risk
        self.visited = False
        self.dist = sys.maxsize
        self.prev = None
        self.connections = []

    def set_visited(self):
        self.visited = True

    def __str__(self):
        description =  f"Loc {self.coords} Risk {self.risk} Visited: {self.visited} Connections:"

        for c in self.connections:
            #description += f"({c.coords[0]}, {c.coords[1]}), "
            description += f"{c.coords}, "

        return description

    def add_connections(self, connections):
        self.connections = connections


def collect_neighbours(coord, graph):
    x, y = coord

    connection_coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    connections = []
    for coords in connection_coords:
        if coords in graph:
            connections.append(graph[coords])

    return connections


def input_to_graph(input):
    graph = {}
    for x in range(0, len(input)):
        for y in range(0, len(input[x])):
            coord = (x, y)
            graph[coord] = Node(coord, input[x][y])

    #connect nodes
    for c in graph.values():
        connections = collect_neighbours(c.coords, graph)
        c.add_connections(connections)

    return graph


def find_next_from_queue(carry: Node, b: Node):
    if carry.dist > b.dist:
        return b

    return carry

def backtrack(target):
    shortest_path = []
    total_risk = 0
    current = target
    while True:
        if current.coords == (0, 0):
            break

        shortest_path.append(current)
        total_risk += current.risk
        current = current.prev

    return shortest_path, total_risk

def calculate_risk_level_to_target(start, target):
    queue = [start]
    while queue:
        current = reduce(find_next_from_queue, queue)
        queue.remove(current)
        current.visited = True

        if current.coords == target:
            print("Target reached!")
            shortest_path, total_risk = backtrack(current)
            return total_risk

        for neighbour in current.connections:
            alt_dist = current.dist + neighbour.risk

            if not neighbour.visited and neighbour not in queue:
                queue.append(neighbour)

            if alt_dist < neighbour.dist:
                neighbour.dist = alt_dist
                neighbour.prev = current

def part1():
    input = read_input("inputs/day15.txt")
    cavern = input_to_graph(input)
    start = cavern[(0, 0)]
    start.dist = 0

    target = (len(input) - 1, len(input[0]) - 1)
    total_risk = calculate_risk_level_to_target(start, target)

    print(f"Day 15, part 1: {total_risk}")








if __name__ == '__main__':
    part1()