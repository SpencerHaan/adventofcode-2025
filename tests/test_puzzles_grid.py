import unittest

import puzzles

TEST_GRID = """\
123
345\
"""

class PuzzlesGridTest(unittest.TestCase):
    @staticmethod
    def test_from_string():
        grid = puzzles.Grid.from_string(TEST_GRID)
        print(grid)

    def test_setitem_in_bounds(self):
        expected = "@"

        grid = puzzles.Grid({}, 3, 3)
        grid[1, 1] = expected

        actual = grid[1, 1]

        self.assertEqual(expected, actual)

    def test_setitem_out_of_bounds(self):
        grid = puzzles.Grid(dict(), 3, 3)

        self.assertRaises(KeyError, grid.__setitem__, (3, 3), "@")

    def test_getitem_in_bounds(self):
        expected = "@"
        grid = puzzles.Grid({(1, 1): expected}, 3, 3)

        actual = grid[1, 1]

        self.assertEqual(expected, actual)

    def test_getitem_out_of_bounds(self):
        grid = puzzles.Grid({(1, 1): "@"}, 3, 3)

        self.assertRaises(KeyError, grid.__getitem__, (3, 3))


if __name__ == '__main__':
    unittest.main()
