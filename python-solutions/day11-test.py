import unittest
from day11 import *

class MyTestCase(unittest.TestCase):
    def test_adjacent_coords(self):
        octopuses = read_input("inputs/day11-example.txt")
        adjacent = adjacent_coords(octopuses, (1, 1))
        self.assertEqual(8, len(adjacent))

        adjacent = adjacent_coords(octopuses, (0, 0))
        self.assertEqual(3, len(adjacent))

        adjacent = adjacent_coords(octopuses, (0, 1))
        self.assertEqual(5, len(adjacent))

        adjacent = adjacent_coords(octopuses, (9, 0))
        self.assertEqual(3, len(adjacent))

        adjacent = adjacent_coords(octopuses, (9, 1))
        self.assertEqual(5, len(adjacent))

        adjacent = adjacent_coords(octopuses, (9, 1))
        self.assertNotIn((9, 1), adjacent)

    def test_flash(self):
        octopuses = [
            [1, 1, 9],
            [1, 10, 1],
            [1, 1, 1]
        ]

        flashes = flash(octopuses, (1, 1))
        self.assertEqual(2, flashes)
        octopuses_after = [
            [2, 3, 0],
            [2, 0, 3],
            [2, 2, 2]
        ]
        self.assertEqual(octopuses_after, octopuses)


if __name__ == '__main__':
    unittest.main()
