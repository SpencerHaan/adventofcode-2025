import unittest

import day_9
from puzzles import Point2D


class Day9Test(unittest.TestCase):
    def test_calculate_area(self):
        test_cases = [
            (Point2D(2, 5), Point2D(9, 7), 24),
            (Point2D(7, 1), Point2D(11, 7), 35),
            (Point2D(7, 3), Point2D(2, 3), 6),
            (Point2D(2, 5), Point2D(11, 1), 50),
        ]
        for a, b, expected_area in test_cases:
            with self.subTest(a=a, b=b, expected_area=expected_area):
                actual_area = day_9.calculate_area(a, b)

                self.assertEqual(expected_area, actual_area)

    def test_find_largest_area(self):
        points = [
            Point2D(7, 1),
            Point2D(11, 1),
            Point2D(11, 7),
            Point2D(9, 7),
            Point2D(9, 5),
            Point2D(2, 5),
            Point2D(2, 3),
            Point2D(7, 3),
        ]

        expected_largest_area = 50

        actual_largest_area = day_9.find_largest_area(points)

        self.assertEqual(expected_largest_area, actual_largest_area)


if __name__ == '__main__':
    unittest.main()
