import textwrap
import unittest

import day_7
import puzzles


class Day7Test(unittest.TestCase):
    def test_split_beam(self):
        test_cases = [
            ((2, 3), [(1, 3), (3, 3)]),
            ((4, 0), [(3, 0), (5, 0)]),
            ((1, 10), [(0, 10), (2, 10)]),
        ]
        for point, expected in test_cases:
            with self.subTest(test_case=point, expected=expected):
                actual = day_7.split_beam(point)

                self.assertEqual(expected, actual)

    def test_analyze_manifold(self):
        diagram = textwrap.dedent("""\
            .......S.......
            ...............
            .......^.......
            ...............
            ......^.^......
            ...............
            .....^.^.^.....
            ...............
            ....^.^...^....
            ...............
            ...^.^...^.^...
            ...............
            ..^...^.....^..
            ...............
            .^.^.^.^.^...^.
            ...............""")
        diagram = puzzles.Grid.from_string(diagram)

        expected_total_splits = 21

        actual_total_splits = day_7.analyze_manifold(diagram)

        self.assertEqual(expected_total_splits, actual_total_splits)


if __name__ == '__main__':
    unittest.main()
