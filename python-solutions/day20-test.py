import unittest
from day20 import *

class Day20TestCase(unittest.TestCase):
    def test_take_comparison_area(self):
        algorithm, image = read_input("inputs/day20-example.txt")

        area = take_comparison_area((-1, -1), image, ".")
        self.assertEqual("........#", area)

        area = take_comparison_area((0, -1), image, ".")
        self.assertEqual(".......#.", area)

        area = take_comparison_area((2, 2), image, ".")
        self.assertEqual("...#...#.", area)

    def test_get_enhancement_pixed(self):
        algorithm, image = read_input("inputs/day20-example.txt")

        area = take_comparison_area((-1, -1), image, ".")
        self.assertEqual(".", get_enhancement_pixel(algorithm, area))

        area = take_comparison_area((0, -1), image, ".")
        self.assertEqual("#", get_enhancement_pixel(algorithm, area))

        area = take_comparison_area((2, 2), image, ".")
        self.assertEqual("#", get_enhancement_pixel(algorithm, area))

    def test_enhance(self):
        algorithm, image = read_input("inputs/day20-example.txt")
        enhanced = enhance(image, algorithm, ".")

        #self.assertEqual([
        #    list(".##.##."),
        #    list("#..#.#."),
        #    list("##.#..#"),
        #    list("####..#"),
        #    list(".#..##."),
        #    list("..##..#"),
        #    list("...#.#.")
        #], enhanced)

    def test_part1_example(self):
        algorithm, image = read_input("inputs/day20-example.txt")

        enhanced = enhance(image, algorithm, ".")
        enhanced = enhance(enhanced, algorithm, ".")

        self.assertEqual(35, count_lit(enhanced))

    def test_part2_example(self):
        algorithm, image = read_input("inputs/day20-example.txt")
        enhanced = enhance_times(image, algorithm, 50)

        self.assertEqual(3351, count_lit(enhanced))



if __name__ == '__main__':
    unittest.main()
