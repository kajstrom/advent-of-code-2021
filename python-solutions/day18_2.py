import math

def read_input(file):
    with open(file) as f:
        return list(map(eval, f.read().splitlines()))

class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.value = None

    def set_left_child(self, left):
        self.left = left
        left.parent = self

    def set_right_child(self, right):
        self.right = right
        right.parent = self

    def has_children(self):
        return self.left is not None and self.right is not None

    def is_regular(self):
        return self.value is not None

    def is_branch(self):
        return self.value is None

    def replace(self, replacement):
        if self.parent.left is self:
            self.parent.set_left_child(replacement)
        else:
            self.parent.set_right_child(replacement)

    def magnitude(self):
        #left_mag = 0
        if self.left.is_branch():
            left_mag = self.left.magnitude()
        else:
            left_mag = self.left.value

        #right_mag = 0
        if self.right.is_branch():
            right_mag = self.right.magnitude()
        else:
            right_mag = self.right.value

        return 3 * left_mag + 2 * right_mag

    def to_list(self):
        if self.is_branch():
            return [
                self.left.to_list(),
                self.right.to_list()
            ]
        else:
            return self.value

    def __str__(self):
        if self.is_branch():
            return f"Left: {self.left} Right: {self.right}"

        return f"Value {self.value}"


def is_list(x):
    return type(x) == list


def is_int(x):
    return type(x) == int

def is_node(x):
    return isinstance(x, Node)


def find_explodable(root, depth=1):
    if root.left.is_branch():
        if depth == 4:
            return root.left

        to_explode = find_explodable(root.left, depth + 1)
        if to_explode is not None:
            return to_explode

    if root.right.is_branch():
        if depth == 4:
            return root.right

        return find_explodable(root.right, depth + 1)

    return None


def flatten(tree: Node, nodes):
    nodes.append(tree)

    if tree.left.is_branch():
        flatten(tree.left, nodes)
    else:
        nodes.append(tree.left)

    if tree.right.is_branch():
        flatten(tree.right, nodes)
    else:
        nodes.append(tree.right)

    return nodes


def find_left_regular(root, until):
    nodes = flatten(root, [])
    stop_at = nodes.index(until)
    left_nodes = nodes[:stop_at]
    left_nodes = reversed(left_nodes)

    for node in left_nodes:
        if node.is_regular():
            return node

    return None


def find_right_regular(root, start):
    nodes = flatten(root, [])
    start_from = nodes.index(start)
    right_nodes = nodes[start_from + 3:]

    for node in right_nodes:
        if node.is_regular():
            return node

    return None

def explode(root):
    to_explode = find_explodable(root)
    if to_explode is None:
        return False

    left_regular = find_left_regular(root, to_explode)
    right_regular = find_right_regular(root, to_explode)

    if left_regular is not None:
        left_regular.value += to_explode.left.value

    if right_regular is not None:
        right_regular.value += to_explode.right.value

    exploded = Node()
    exploded.value = 0
    to_explode.replace(exploded)

    return True

def split(root):
    nodes = flatten(root, [])
    for node in nodes:
        if node.is_regular():
            if node.value >= 10:
                splitted = Node()
                left = Node()
                right = Node()

                left.value = math.floor(node.value / 2)
                right.value = math.ceil(node.value / 2)

                splitted.set_left_child(left)
                splitted.set_right_child(right)

                node.replace(splitted)
                return True

    return False

def add(tree_a, tree_b):
    root = Node()
    root.set_left_child(tree_a)
    root.set_right_child(tree_b)

    while True:
        exploded = explode(root)
        if exploded:
            continue

        splitted = split(root)
        if splitted:
            continue

        return root


def add_all(snailfishes):
    trees = []
    for sf in snailfishes:
        root = Node()
        build_tree(sf, root)
        trees.append(root)

    current = trees[0]
    for t in trees[1:]:
        current = add(current, t)

    return current


def largest_combination_magnitude(snailfishes):
    magnitudes = []
    largest_magnitude = 0
    for current_s in snailfishes:
        for t_s in snailfishes:

            if current_s != t_s:
                current = Node()
                build_tree(current_s, current)
                t = Node()
                build_tree(t_s, t)

                combined1 = add(current, t)
                mag = combined1.magnitude()
                magnitudes.append(mag)
                if mag > largest_magnitude:
                    largest_magnitude = mag

    return largest_magnitude

def build_tree(pairs, root: Node):
    left, right = pairs

    left_node = Node()
    if is_list(left):
        build_tree(left, left_node)
    else:
        left_node.value = left

    right_node = Node()
    if is_list(right):
        build_tree(right, right_node)
    else:
        right_node.value = right

    root.set_left_child(left_node)
    root.set_right_child(right_node)

if __name__ == '__main__':
    snailfishes = read_input("inputs/day18.txt")
    final = add_all(snailfishes)
    print(f"Day 18, part 1: {final.magnitude()}")
    print(f"Day 18, part 2 {largest_combination_magnitude(snailfishes)}")