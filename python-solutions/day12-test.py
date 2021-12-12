import unittest
from day12 import *


class Day12TestCase(unittest.TestCase):
    def test_can_visit(self):
        path = ["start", "A", "end"]
        self.assertFalse(can_visit_small_twice("start", path))
        self.assertFalse(can_visit_small_twice("end", path))
        self.assertTrue(can_visit_small_twice("A", path))

    def test_can_visit_small_caves(self):
        path = ["a"]
        self.assertTrue(can_visit_small_twice("a", path))
        path = ["a", "a"]
        self.assertFalse(can_visit_small_twice("a", path))
        self.assertTrue(can_visit_small_twice("b", path))
        path = ["a", "a", "b"]
        self.assertFalse(can_visit_small_twice("b", path))


if __name__ == '__main__':
    unittest.main()
