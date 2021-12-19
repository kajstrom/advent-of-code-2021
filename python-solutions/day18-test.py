import unittest
from day18 import *

class Day18v2TestCase(unittest.TestCase):
    def test_build_tree(self):
        root = Node()
        build_tree([1, 2], root)

        self.assertEqual(1, root.left.value)
        self.assertEqual(2, root.right.value)

        root = Node()
        build_tree([[1, 2], 3], root)

        self.assertEqual(3, root.right.value)
        self.assertIsNotNone(root.left.left)
        self.assertIsNotNone(root.left.right)
        self.assertTrue(root.__eq__(root.left.parent))

    def test_find_explodable(self):
        root = Node()
        build_tree([[[[[9, 8], 1], 2], 3], 4], root)

        to_explode = find_explodable(root)
        self.assertEqual(9, to_explode.left.value)
        self.assertEqual(8, to_explode.right.value)

        root = Node()
        build_tree([7,[6,[5,[4,[3,2]]]]], root)

        to_explode = find_explodable(root)
        self.assertEqual(3, to_explode.left.value)
        self.assertEqual(2, to_explode.right.value)

        root = Node()
        build_tree([[6,[5,[4,[3,2]]]],1], root)

        to_explode = find_explodable(root)
        self.assertEqual(3, to_explode.left.value)
        self.assertEqual(2, to_explode.right.value)

        root = Node()
        build_tree([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]], root)
        to_explode = find_explodable(root)
        self.assertEqual(4, to_explode.left.value)
        self.assertEqual(3, to_explode.right.value)

    def test_flatten(self):
        root = Node()
        build_tree([[[[[9, 8], 1], 2], 3], 4], root)

        nodes = flatten(root, [])

        self.assertIsNotNone(nodes)

    def test_find_left_regular(self):
        root = Node()
        build_tree([[[[[9, 8], 1], 2], 3], 4], root)

        to_explode = find_explodable(root)
        self.assertIsNone(find_left_regular(root, to_explode))

        root = Node()
        build_tree([[6,[5,[4,[3,2]]]],1], root)

        to_explode = find_explodable(root)
        left_regular = find_left_regular(root, to_explode)
        self.assertEqual(4, left_regular.value)

    def test_find_right_regular(self):
        root = Node()
        build_tree([[[[[9, 8], 1], 2], 3], 4], root)

        to_explode = find_explodable(root)
        right_regular = find_right_regular(root, to_explode)
        self.assertEqual(1, right_regular.value)

    def test_explode(self):
        root = Node()
        build_tree([[[[[9, 8], 1], 2], 3], 4], root)
        self.assertTrue(explode(root))
        self.assertFalse(explode(root))

        self.assertEqual([[[[0,9],2],3],4], root.to_list())

        root = Node()
        build_tree([7,[6,[5,[4,[3,2]]]]], root)
        self.assertTrue(explode(root))
        self.assertEqual([7,[6,[5,[7,0]]]], root.to_list())

        root = Node()
        build_tree([[6,[5,[4,[3,2]]]],1], root)
        self.assertTrue(explode(root))
        self.assertEqual([[6,[5,[7,0]]],3], root.to_list())

        root = Node()
        build_tree([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], root)
        self.assertTrue(explode(root))
        self.assertEqual([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], root.to_list())
        self.assertTrue(explode(root))
        self.assertEqual([[3,[2,[8,0]]],[9,[5,[7,0]]]], root.to_list())

    def test_split(self):
        root = Node()
        build_tree([[[[0,7],4],[15,[0,13]]],[1,1]], root)
        self.assertTrue(split(root))
        self.assertEqual([[[[0,7],4],[[7,8],[0,13]]],[1,1]], root.to_list())
        self.assertTrue(split(root))
        self.assertEqual([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]], root.to_list())
        self.assertFalse(split(root))

    def test_add(self):
        tree_a = Node()
        build_tree([[[[4,3],4],4],[7,[[8,4],9]]], tree_a)
        tree_b = Node()
        build_tree([1,1], tree_b)

        root = add(tree_a, tree_b)
        self.assertEqual([[[[0,7],4],[[7,8],[6,0]]],[8,1]], root.to_list())

    def test_example1(self):
        root = add_all([
            [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
            [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
            [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
            [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
            [7, [5, [[3, 8], [1, 4]]]],
            [[2, [2, 2]], [8, [8, 1]]],
            [2, 9],
            [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
            [[[5, [7, 4]], 7], 1],
            [[[[4, 2], 2], 6], [8, 7]]
        ])

        self.assertEqual([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], root.to_list())

    def test_example2(self):
        root = add_all([
            [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
            [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
            [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
            [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
            [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
            [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
            [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
            [[9, 3], [[9, 9], [6, [4, 9]]]],
            [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
            [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]],
        ])

        self.assertEqual([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]], root.to_list())
        self.assertEqual(4140, root.magnitude())

    def test_magnitude(self):
        root = Node()
        build_tree([9,1], root)
        self.assertEqual(29, root.magnitude())

        root = Node()
        build_tree([[9,1],[1,9]], root)
        self.assertEqual(129, root.magnitude())

        root = Node()
        build_tree([[1,2],[[3,4],5]], root)
        self.assertEqual(143, root.magnitude())

        root = Node()
        build_tree([[[[0,7],4],[[7,8],[6,0]]],[8,1]], root)
        self.assertEqual(1384, root.magnitude())

        root = Node()
        build_tree([[[[1,1],[2,2]],[3,3]],[4,4]], root)
        self.assertEqual(445, root.magnitude())

        root = Node()
        build_tree([[[[3,0],[5,3]],[4,4]],[5,5]], root)
        self.assertEqual(791, root.magnitude())

        root = Node()
        build_tree([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], root)
        self.assertEqual(3488, root.magnitude())

    def test_part1(self):
        snailfishes = read_input("inputs/day18.txt")
        final = add_all(snailfishes)
        self.assertEqual(4202, final.magnitude())

    def test_part2_example(self):
        magnitude = largest_combination_magnitude([
            [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
            [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
            [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
            [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
            [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
            [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
            [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
            [[9, 3], [[9, 9], [6, [4, 9]]]],
            [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
            [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]]
        ])

        self.assertEqual(3993, magnitude)

    def test_part2(self):
        snailfishes = read_input("inputs/day18.txt")
        self.assertEqual(4779, largest_combination_magnitude(snailfishes))


if __name__ == '__main__':
    unittest.main()
