def read_input(file: str):
    with open(file) as f:
        return list(map(lambda s: s.split("-"), f.read().splitlines()))


def connect_nodes(graph: dict[str, list[str]], connection):
    a, b = connection

    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)


def find_paths_from_start_to_end(graph, can_visit_fn):
    queued_paths = [["start"]]
    complete_paths = []
    iter = 0
    while len(queued_paths) > 0:
        #if iter % 10000 == 0:
        #    print(f"Iter {iter} Completed {len(complete_paths)} in queue: {len(queued_paths)}")

        current_path = queued_paths.pop()
        current_cave = current_path[-1]

        if current_cave == "end":
            complete_paths.append(current_path)
            continue

        connected = graph[current_cave]

        visitable_connections = []
        for cave in connected:
            if can_visit_fn(cave, current_path):
                visitable_connections.append(cave)

        if len(visitable_connections) == 0:
            #Dead end, nothing to visit
            continue

        # queue other options
        for cave in visitable_connections:
            to_queue = list(current_path)
            to_queue.append(cave)
            queued_paths.append(to_queue)

        iter += 1

    return complete_paths


def can_visit_small_once(cave, path: list[str]):
    if cave.islower():
        return cave not in path
    else:
        return True


def part1():
    connections = read_input("inputs/day12.txt")

    graph = dict()
    for connection in connections:
        connect_nodes(graph, connection)

    paths = find_paths_from_start_to_end(graph, can_visit_small_once)

    print(f"Day 12, part 1: {len(paths)}")


def can_visit_small_twice(cave, path: list[str]):
    if cave == "start" or cave == "end":
        return cave not in path

    if cave.islower():
        # single small cave can be visited at most ones
        lower_caves_in_path = []
        lower_visited_twice = False
        for c in path:
            if c.islower():
                if c in lower_caves_in_path:
                    lower_visited_twice = True
                    break
                lower_caves_in_path.append(c)

        return cave not in path or not lower_visited_twice

    return True


def part2():
    connections = read_input("inputs/day12.txt")

    graph = dict()
    for connection in connections:
        connect_nodes(graph, connection)

    paths = find_paths_from_start_to_end(graph, can_visit_small_twice)

    print(f"Day 12, part 2: {len(paths)}")


if __name__ == '__main__':
    part1()
    part2()
