import unittest

import day_2

class TestDay1(unittest.TestCase):
    def test_find_invalid_ids(self):
        test_cases = [
            (11, 22, [11, 22]),
            (95, 115, [99]),
            (998, 1012, [1010]),
            (1188511880, 1188511890, [1188511885]),
            (222220, 222224, [222222]),
            (446443, 446449, [446446]),
            (38593856, 38593862, [38593859]),
            (1698522, 1698528, []),
            (824824821, 824824827, []),
            (2121212118, 2121212124, []),
            (26, 76, [33, 44, 55, 66]),
        ]

        for lower, upper, expected_invalid_ids in test_cases:
            with self.subTest(test_case=(lower, upper), expected_invalid_ids=expected_invalid_ids):
                actual_invalid_ids = day_2.find_invalid_ids(lower, upper)

                self.assertEqual(expected_invalid_ids, actual_invalid_ids)
