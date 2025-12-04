import unittest

import day_4

GRID = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.\
""".split("\n")

ROWS = len(GRID)
COLS = len(GRID[0])


class TestDay4(unittest.TestCase):
    def test_is_roll_accessible(self):
        test_cases = [
            ((2, 0), True),
            ((3, 0), True),
            ((5, 0), True),
            ((6, 0), True),
            ((8, 0), True),
            ((0, 1), True),
            ((6, 2), True),
            ((0, 4), True),
            ((9, 4), True),
            ((0, 7), True),
            ((0, 9), True),
            ((2, 9), True),
            ((8, 9), True),
        ]
        for position, expected in test_cases:
            with self.subTest(test_case=position, expected=expected):
                actual = day_4.is_roll_accessible(GRID, position, (COLS, ROWS))

                self.assertEqual(expected, actual)

    def test_find_inaccessible_rolls(self):
        expected = [
            (2, 0),
            (3, 0),
            (5, 0),
            (6, 0),
            (8, 0),
            (0, 1),
            (6, 2),
            (0, 4),
            (9, 4),
            (0, 7),
            (0, 9),
            (2, 9),
            (8, 9),
        ]

        actual = day_4.find_inaccessible_rolls(GRID)

        self.assertEqual(len(expected), len(actual))
        self.assertEqual(sorted(expected), sorted(actual))


if __name__ == '__main__':
    unittest.main()
