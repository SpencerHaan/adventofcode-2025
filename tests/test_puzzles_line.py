import unittest

from puzzles import Line, Point2D


class LineTest(unittest.TestCase):
    def test_is_intersecting(self):
        test_cases = [
            (Line(Point2D(0, 1), Point2D(2, 1)), Line(Point2D(1, 0), Point2D(1, 2)), True),
            (Line(Point2D(1, 0), Point2D(1, 2)), Line(Point2D(0, 1), Point2D(2, 1)), True),
            (Line(Point2D(0, 1), Point2D(2, 1)), Line(Point2D(0, 2), Point2D(2, 2)), False),
            (Line(Point2D(1, 0), Point2D(1, 2)), Line(Point2D(2, 0), Point2D(2, 2)), False),
        ]
        for line_a, line_b, expected in test_cases:
            with self.subTest(test_case=(line_a, line_b), expected=expected):
                actual = line_a.is_intersecting(line_b)

                self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
