import unittest
from day17 import *

class Day17TestCase(unittest.TestCase):
    def test_parse_target_area(self):
        target_area = parse_target_area("target area: x=20..30, y=-10..-5")

        self.assertIn(20, target_area["x"])
        self.assertIn(30, target_area["x"])
        self.assertNotIn(19, target_area["x"])
        self.assertNotIn(31, target_area["x"])

        self.assertIn(-10, target_area["y"])
        self.assertIn(-5, target_area["y"])
        self.assertNotIn(-11, target_area["y"])
        self.assertNotIn(-4, target_area["y"])


    def test_update_velocity(self):
        self.assertEqual((5, 5), update_velocity((6, 6)))
        self.assertEqual((0, -2), update_velocity((1, -1)))
        self.assertEqual((0, -3), update_velocity((0, -2)))


    def test_target_passed(self):
        target_area = parse_target_area("target area: x=20..30, y=-10..-5")
        self.assertTrue(target_passed((35, -15), target_area))
        self.assertTrue(target_passed((35, -3), target_area))
        self.assertTrue(target_passed((15, -15), target_area))

        self.assertFalse(target_passed((15, -3), target_area))
        self.assertFalse(target_passed((25, -6), target_area))


    def test_in_target(self):
        target_area = parse_target_area("target area: x=20..30, y=-10..-5")
        self.assertTrue(in_target((20, -10), target_area))
        self.assertTrue(in_target((25, -7), target_area))
        self.assertTrue(in_target((30, -5), target_area))

        self.assertFalse(in_target((19, -4), target_area))



    def test_fire_probe(self):
        target_area = parse_target_area("target area: x=20..30, y=-10..-5")
        target_hit, trajectory = fire_probe((7, 2), target_area)

        self.assertTrue(target_hit)
        self.assertEqual(7, len(trajectory))

        target_hit, trajectory = fire_probe((6, 3), target_area)
        self.assertTrue(target_hit)
        self.assertEqual(9, len(trajectory))

        target_hit, trajectory = fire_probe((9, 0), target_area)
        self.assertTrue(target_hit)
        self.assertEqual(4, len(trajectory))

        target_hit, trajectory = fire_probe((17, -4), target_area)
        self.assertFalse(target_hit)
        self.assertEqual(2, len(trajectory))


    def test_find_highest_y_point(self):
        target_area = parse_target_area("target area: x=20..30, y=-10..-5")
        valid_trajectories = find_valid_trajectories(target_area)
        self.assertEqual(45, find_highest_y_point(valid_trajectories))



if __name__ == '__main__':
    unittest.main()
