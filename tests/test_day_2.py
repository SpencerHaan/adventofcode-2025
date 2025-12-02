import unittest

import day_2

class TestDay1(unittest.TestCase):
    def test_find_place_value_divisors(self):
        test_cases = [
            (1, [1]),
            (2, [1]),
            (3, [1]),
            (4, [1, 2]),
            (6, [1, 2, 3]),
            (12, [1, 2, 3, 4, 6]),
        ]

        for length, expected_divisors in test_cases:
            with self.subTest(test_case=length, expected_divisors=expected_divisors):
                actual_divisors = day_2.find_place_value_divisors(length)

                self.assertEqual(actual_divisors, expected_divisors)

    def test_find_invalid_ids(self):
        test_cases = [
            (11, 22, [11, 22]),
            (95, 115, [99, 111]),
            (998, 1012, [999, 1010]),
            (1188511880, 1188511890, [1188511885]),
            (222220, 222224, [222222]),
            (1698522, 1698528, []),
            (446443, 446449, [446446]),
            (38593856, 38593862, [38593859]),
            (565653, 565659, [565656]),
            (824824821, 824824827, [824824824]),
            (2121212118, 2121212124, [2121212121]),
            (26, 76, [33, 44, 55, 66]),
            (2, 17, [11])
        ]

        for lower, upper, expected_invalid_ids in test_cases:
            with self.subTest(test_case=(lower, upper), expected_invalid_ids=expected_invalid_ids):
                actual_invalid_ids = sorted(day_2.find_invalid_ids(lower, upper))

                self.assertEqual(expected_invalid_ids, actual_invalid_ids)
