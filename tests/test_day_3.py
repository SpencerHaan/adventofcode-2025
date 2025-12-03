import unittest

import day_3


class TestDay3(unittest.TestCase):
    def test_find_largest_joltage(self):
        test_cases = [
            ("987654321111111", 2, 98),
            ("811111111111119", 2, 89),
            ("234234234234278", 2, 78),
            ("818181911112111", 2, 92),
            ("2232212212212222211221231124224222213132222133122224222123222112324122222122221322222225222342243112", 2, 54),
            ("987654321111111", 3, 987),
            ("811111111111119", 3, 819),
            ("987654321111111", 12, 987654321111),
            ("811111111111119", 12, 811111111119),
            ("234234234234278", 12, 434234234278),
            ("818181911112111", 12, 888911112111),
        ]
        for battery_bank, max_battery_count, expected_joltage in test_cases:
            with self.subTest(test_case=battery_bank, max_battery_count=max_battery_count, expected_joltage=expected_joltage):
                actual_joltage = day_3.find_largest_joltage(battery_bank, max_battery_count)

                self.assertEqual(expected_joltage, actual_joltage)


if __name__ == '__main__':
    unittest.main()
