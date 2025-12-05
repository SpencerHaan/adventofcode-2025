import unittest

import day_5


class TestDay5(unittest.TestCase):
    def test_is_fresh(self):
        db = day_5.IngredientDb([
            range(3, 6),
            range(10, 15),
            range(16, 21),
            range(12, 19),
        ])
        test_cases = [
            (1, False),
            (5, True),
            (8, False),
            (11, True),
            (17, True),
            (32, False),
        ]

        for available_ingredient, expected_is_fresh in test_cases:
            with self.subTest(available_ingredient=available_ingredient, expected_is_fresh=expected_is_fresh):
                actual_is_fresh = db.is_fresh(available_ingredient)

                self.assertEqual(expected_is_fresh, actual_is_fresh)


if __name__ == '__main__':
    unittest.main()
