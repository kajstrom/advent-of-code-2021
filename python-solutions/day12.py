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


def find_paths_from_start_to_end(graph):
    queued_paths = [["start"]]
    complete_paths = []
    while len(queued_paths) > 0:
        current_path = queued_paths[0]
        queued_paths = queued_paths[1:]

        current_cave = current_path[-1]
        if current_cave == "end":
            complete_paths.append(current_path)

        connected = graph[current_cave]
        #print(connected)

        # queue other options
        for cave in connected:
            if cave.islower() and cave in current_path:
                continue

            to_queue = list(current_path)
            to_queue.append(cave)
            queued_paths.append(to_queue)

    return complete_paths

def part1():
    connections = read_input("inputs/day12.txt")
    print(connections)

    graph = dict()
    for connection in connections:
        connect_nodes(graph, connection)

    paths = find_paths_from_start_to_end(graph)

    print(f"Day 12, part 1: {len(paths)}")



if __name__ == '__main__':
    part1()