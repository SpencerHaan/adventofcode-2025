import unittest

import day_5

TEST_RANGES = [
    range(3, 6),
    range(10, 15),
    range(16, 21),
    range(12, 19),
]

class TestDay5(unittest.TestCase):
    def test_is_fresh(self):
        test_cases = [
            (1, False),
            (5, True),
            (8, False),
            (11, True),
            (17, True),
            (32, False),
        ]
        db = day_5.IngredientDb(TEST_RANGES)
        for available_ingredient, expected_is_fresh in test_cases:
            with self.subTest(test_case=available_ingredient, expected_is_fresh=expected_is_fresh):
                actual_is_fresh = db.is_fresh(available_ingredient)

                self.assertEqual(expected_is_fresh, actual_is_fresh)

    def test_considered_fresh(self):
        expected_considered_fresh = 14

        db = day_5.IngredientDb(TEST_RANGES)

        actual_considered_fresh = db.considered_fresh()

        self.assertEqual(expected_considered_fresh, actual_considered_fresh)

    def test_range_edge_cases(self):
        test_cases = [
            # One range inside another
            ([range(1, 10), range(3, 7)], 9),
            # One range overlaps the other
            ([range(1, 7), range(3, 10)], 9),
            # One range has a single gap between another
            ([range(1, 5), range(6, 10)], 8),
            # One range starts where another stops
            ([range(1, 6), range(5, 10)], 9),
            # Both ranges start the same but end differently
            ([range(1, 6), range(1, 10)], 9),
            # Both ranges start differently but end the same
            ([range(1, 10), range(6, 10)], 9),
        ]
        for test_ranges, expected in test_cases:
            with self.subTest(test_case=test_ranges, expected=expected):
                db = day_5.IngredientDb(test_ranges)

                actual = db.considered_fresh()

                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
