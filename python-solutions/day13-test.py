import unittest
from day13 import *

class Day13TestCase(unittest.TestCase):
    def test_fold_y(self):
        self.assertEqual((2, 0), fold_y(7, (2, 14)))
        self.assertEqual((2, 6), fold_y(7, (2, 8)))
        self.assertEqual((2, 7), fold_y(7, (2, 7)))

    def test_fold_x(self):
        self.assertEqual((4, 0),fold_x(5, (6, 0)))
        self.assertEqual((1, 0), fold_x(5, (9, 0)))

    def test_example(self):
        dots, folds = read_input("inputs/day13-example.txt")
        folded_dots = fold([folds[0]], dots)
        self.assertEqual(17, count_visible(folded_dots))

    def test_example2(self):
        dots, folds = read_input("inputs/day13-example.txt")
        folded = fold(folds, dots)
        self.assertEqual(16, count_visible(folded))

if __name__ == '__main__':
    unittest.main()
