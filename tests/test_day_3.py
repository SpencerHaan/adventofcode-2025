import unittest

import day_3


class TestDay3(unittest.TestCase):
    def test_something(self):
        test_cases = [
            ("987654321111111", 98),
            ("811111111111119", 89),
            ("234234234234278", 78),
            ("818181911112111", 92),
            ("2232212212212222211221231124224222213132222133122224222123222112324122222122221322222225222342243112", 54),
        ]
        for battery_bank, expected_joltage in test_cases:
            with self.subTest(test_case=battery_bank, expected_joltage=expected_joltage):
                actual_joltage = day_3.find_largest_joltage(battery_bank)

                self.assertEqual(expected_joltage, actual_joltage)


if __name__ == '__main__':
    unittest.main()
