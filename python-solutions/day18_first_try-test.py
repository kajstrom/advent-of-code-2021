import unittest
from day18_first_try import *


class Day18TestCase(unittest.TestCase):
    def skip_test_explode(self):
        pair, exploded = explode([[[[[9, 8], 1], 2], 3], 4])
        self.assertEqual([[[[0, 9], 2], 3], 4], pair)
        self.assertTrue(exploded)

        pair, exploded = explode([7, [6, [5, [4, [3, 2]]]]])
        self.assertEqual([7, [6, [5, [7, 0]]]], pair)
        self.assertTrue(exploded)

        pair, exploded = explode([[6, [5, [4, [3, 2]]]], 1])
        self.assertEqual([[6, [5, [7, 0]]], 3], pair)
        self.assertTrue(exploded)

        pair, exploded = explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
        self.assertEqual([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], pair)
        self.assertTrue(exploded)

        pair, exploded = explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
        self.assertEqual([[3,[2,[8,0]]],[9,[5,[7,0]]]], pair)
        self.assertTrue(exploded)

    def test_find_explodable(self):
        path1 = find_explodable([[[[[9, 8], 1], 2], 3], 4], [])
        self.assertEqual([0, 0, 0, 0], path1)

        path2 = find_explodable([7, [6, [5, [4, [3, 2]]]]], [])
        self.assertEqual([1, 1, 1, 1], path2)

        path3 = find_explodable([[6, [5, [4, [3, 2]]]], 1], [])
        self.assertEqual([0, 1, 1, 1], path3)

        self.assertEqual(None, find_explodable([1, 2], []))

        path4 = find_explodable([[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]], [])
        self.assertIsNotNone(path4)

    def test_find_splittable(self):
        pair = [[[[0,7],4],[15,[0,13]]],[1,1]]
        path = find_splittable(pair)
        self.assertEqual([0, 1, 0], path)

    def test_split(self):
        pair = [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
        pair, splitted = split(pair)
        self.assertEqual([7, 8], get_value(pair, [0, 1, 0]))

        pair = [[[[0, 7], 4], [16, [0, 13]]], [1, 1]]
        pair, splitted = split(pair)
        self.assertEqual([8, 8], get_value(pair, [0, 1, 0]))

    def test_get_value(self):
        pair = [[[[[9, 8], 1], 2], 3], 4]
        self.assertEqual([9, 8], get_value(pair, [0, 0, 0, 0]))

    def test_set_value(self):
        pair = [[[[[9, 8], 1], 2], 3], 4]
        set_value(pair, [0, 0, 0, 0], [0, 9])
        self.assertEqual([[[[[0, 9], 1], 2], 3], 4], pair)

    def test_find_left_regular_number(self):
        pair = [[[[[9, 8], 1], 2], 3], 4]
        path = find_explodable(pair, [])
        path_to_regular = find_left_regular_number(pair, path)
        self.assertEqual(None, path_to_regular)

        pair = [7, [6, [5, [4, [3, 2]]]]]
        path = find_explodable(pair, [])
        path_to_regular = find_left_regular_number(pair, path)
        self.assertEqual([1, 1, 1, 0], path_to_regular)

        pair = [7, [6, [5, [[4, 2], [3, 2]]]]]
        path = find_explodable(pair, [])
        path_to_regular = find_left_regular_number(pair, path)
        self.assertEqual([1, 1, 0], path_to_regular)


    def test_find_right_regular_number(self):
        pair = [[[[[9, 8], 1], 2], 3], 4]
        path = find_explodable(pair, [])
        path_to_regular = find_right_regular_number(pair, path)
        self.assertEqual([0, 0, 0, 1], path_to_regular)

        pair = [[6, [5, [4, [3, 2]]]], 1]
        path = find_explodable(pair, [])
        path_to_regular = find_right_regular_number(pair, path)
        self.assertEqual([1], path_to_regular)

        pair = [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
        path = find_explodable(pair, [])
        path_to_regular = find_right_regular_number(pair, path)
        self.assertEqual([1, 0], path_to_regular)

    def test_add(self):
        a = [[[[4,3],4],4],[7,[[8,4],9]]]
        b = [1, 1]
        ab = add(a, b)

        self.assertEqual([[[[0,7],4],[[7,8],[6,0]]],[8,1]], ab)

        a = [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
        b = [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
        ab = add(a, b)

        self.assertEqual([[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]], ab)

    def test_add_example(self):
        snailfishes = [
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
        ]

        current = snailfishes[0]
        for next in snailfishes[1:]:
            current = add(current, next)
            print(current)


    def skip_sum_all(self):
        final = sum_all([
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4]
        ])

        self.assertEqual([[[[1,1],[2,2]],[3,3]],[4,4]], final)

        final = sum_all([
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5]
        ])

        self.assertEqual([[[[3,0],[5,3]],[4,4]],[5,5]], final)

        final = sum_all([
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5],
            [6, 6]
        ])

        self.assertEqual([[[[5,0],[7,4]],[5,5]],[6,6]], final)

        final = sum_all([
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

        self.assertEqual([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]], final)



if __name__ == '__main__':
    unittest.main()
