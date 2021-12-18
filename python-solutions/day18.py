import math


def read_input(file):
    with open(file) as f:
        return list(map(eval, f.read().splitlines()))


def is_list(x):
    return type(x) == list


def is_int(x):
    return type(x) == int


def get_value(pair, path: list[int]):
    current_pair = pair
    for i in path:
        current_pair = current_pair[i]

    return current_pair


def set_value(pair, path: list[int], value):
    current_pair = pair
    path_to_parent = path.copy()
    last_idx = path_to_parent.pop()
    for i in path_to_parent:
        current_pair = current_pair[i]

    current_pair[last_idx] = value


def find_left_regular_number(pair: list, path: list[int]):
    current_path = path.copy()
    current_path.pop()

    queue = []

    if path[-1] != 0:
        # queue lefthand neighbors
            for i in range(path[-1] - 1, -1, -1):
                queue.append(current_path + [i])

    while current_path:
        to_queue_idx = current_path.pop()
        for i in range(to_queue_idx - 1, -1, -1):
            #queue all lefhand side branches
            queue.append(current_path + [i])

    while queue:
        current_path = queue.pop(0)
        #print("From queue", current_path)

        value = get_value(pair, current_path)

        if is_int(value):
            return current_path

        if is_list(value):
            for ci in range(len(value) - 1, -1, -1):
                #print(ci)
                if is_int(value[ci]):
                    return current_path + [ci]

            for ci in range(0, len(value)):
                if is_list(value[ci]):
                    queue.insert(0, current_path + [ci])

    return None


def find_right_regular_number(pair: list, path: list[int]):
    current_path = path.copy()
    current_path.pop()

    queue = []
    #queue righthand neighbors
    for i in range(path[-1] + 1, len(get_value(pair, current_path))):
        queue.append(current_path + [i])

    #queue righthand branches
    while current_path:
        to_queue_idx = current_path.pop()
        for i in range(to_queue_idx + 1, len(get_value(pair, current_path))):
            queue.append(current_path + [i])

    while queue:
        current_path = queue.pop(0)
        value = get_value(pair, current_path)

        if is_int(value):
            return current_path

        if is_list(value):
            for ci in range(0, len(value)):
                if is_int(value[ci]):
                    return current_path + [ci]

            for ci in range(len(value) - 1, -1, -1):
                if is_list(value[ci]):
                    queue.insert(0, current_path + [ci])


    return None


def find_explodable(pair, path):
    queue = []
    for i in range(0, len(pair)):
        queue.append([i])

    while queue:
        current_path = queue.pop(0)
        value = get_value(pair, current_path)

        if len(current_path) == 4:
            if is_list(value):
                return current_path

        if is_list(value):
            for ci in range(len(value) - 1, -1, -1):
                queue.insert(0, current_path + [ci])

    return None


def find_splittable(pair):
    queue = []
    for i in range(0, len(pair)):
        queue.append([i])

    #print(queue)
    while queue:
        current_path = queue.pop(0)
        #print(current_path)
        value = get_value(pair, current_path)
        #print("Value", value)

        if is_int(value) and value >= 10:
            return current_path

        if is_list(value):
            for ci in range(0, len(value)):
                if is_int(value[ci]) and value[ci] >= 10:
                    return current_path + [ci]

            for ci in range(len(value) - 1, -1, -1):
                if is_list(value[ci]):
                    queue.insert(0, current_path + [ci])

    return None


def explode(top_pair):
    path_to_explode = find_explodable(top_pair, [])
    can_explode = path_to_explode is not None

    print(path_to_explode)
    if can_explode:
        left_reg_path = find_left_regular_number(top_pair, path_to_explode)
        right_reg_path = find_right_regular_number(top_pair, path_to_explode)
        left, right = get_value(top_pair, path_to_explode)
        print(left, right)

        if left_reg_path is not None:
            left_reg = get_value(top_pair, left_reg_path)
            set_value(top_pair, left_reg_path, left_reg + left)

        #print(right_reg_path)
        if right_reg_path is not None:
            right_reg = get_value(top_pair, right_reg_path)
            #print(right_reg)
            set_value(top_pair, right_reg_path, right_reg + right)

        set_value(top_pair, path_to_explode, 0)

    return top_pair, can_explode


def split(top_pair):
    path_to_split = find_splittable(top_pair)
    can_split = path_to_split is not None

    if can_split:
        value = get_value(top_pair, path_to_split)
        left = math.floor(value / 2)
        right = math.ceil(value / 2)
        set_value(top_pair, path_to_split, [left, right])

    return top_pair, can_split

def add(a, b):
    ab = [a, b]

    step = 1
    while True:
        #print(f"Step {step}")
        step += 1

        ab, exploded = explode(ab)
        if exploded:
            print("Exploded")
            continue

        ab, splitted = split(ab)

        if splitted:
            print("Splitted")
            continue

        if not exploded and not splitted:
            #print("No exploding or splitting possible")
            break

    return ab


def sum_all(snailfishes):
    current = snailfishes[0]
    for next in snailfishes[1:]:
        current = add(current, next)

    return current


if __name__ == '__main__':
    print(read_input("inputs/day18.txt"))