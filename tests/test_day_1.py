import unittest

import day_1

class TestDay1(unittest.TestCase):
    def test_rotate_dial(self):
        test_cases = [
            ("L68", 1, 82),
            ("L30", 0, 52),
            ("R48", 1, 0),
            ("L5", 0, 95),
            ("R60", 1, 55),
            ("L55", 1, 0),
            ("L1", 0, 99),
            ("L99", 1, 0),
            ("R14", 0, 14),
            ("L82", 1, 32),
        ]
        safe = day_1.Safe(50)

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                instruction, expected_zero_clicks, expected_dial_position = test_case

                actual_zero_clicks = safe.rotate_dial(instruction)
                actual_dial_position = safe.dial_position()

                self.assertEqual(expected_zero_clicks, actual_zero_clicks)
                self.assertEqual(expected_dial_position, actual_dial_position)

    def test_rotate_dial_overflow_at_0_to_0(self):
        expected_zero_clicks = 1
        expected_dial_position = 0

        instruction = "R100"
        starting_dial_position = 0
        safe = day_1.Safe(starting_dial_position)

        actual_zero_clicks = safe.rotate_dial(instruction)
        actual_dial_position = safe.dial_position()

        self.assertEqual(expected_zero_clicks, actual_zero_clicks)
        self.assertEqual(expected_dial_position, actual_dial_position)

    def test_rotate_dial_overflow_at_1_to_1(self):
        expected_zero_clicks = 1
        expected_dial_position = 1

        instruction = "R100"
        starting_dial_position = 1
        safe = day_1.Safe(starting_dial_position)

        actual_zero_clicks = safe.rotate_dial(instruction)
        actual_dial_position = safe.dial_position()

        self.assertEqual(expected_zero_clicks, actual_zero_clicks)
        self.assertEqual(expected_dial_position, actual_dial_position)

    def test_rotate_dial_underflow_at_0_to_0(self):
        expected_zero_clicks = 1
        expected_dial_position = 0

        instruction = "L100"
        starting_dial_position = 0
        safe = day_1.Safe(starting_dial_position)

        actual_zero_clicks = safe.rotate_dial(instruction)
        actual_dial_position = safe.dial_position()

        self.assertEqual(expected_zero_clicks, actual_zero_clicks)
        self.assertEqual(expected_dial_position, actual_dial_position)

    def test_rotate_dial_underflow_at_1_to_1(self):
        expected_zero_clicks = 1
        expected_dial_position = 1

        instruction = "R100"
        starting_dial_position = 1
        safe = day_1.Safe(starting_dial_position)

        actual_zero_clicks = safe.rotate_dial(instruction)
        actual_dial_position = safe.dial_position()

        self.assertEqual(expected_zero_clicks, actual_zero_clicks)
        self.assertEqual(expected_dial_position, actual_dial_position)

    def test_rotate_dial_overflow_at_50_r1000(self):
        expected_zero_clicks = 10
        expected_dial_position = 50

        instruction = "R1000"
        starting_dial_position = 50
        safe = day_1.Safe(starting_dial_position)

        actual_zero_clicks = safe.rotate_dial(instruction)
        actual_dial_position = safe.dial_position()

        self.assertEqual(expected_zero_clicks, actual_zero_clicks)
        self.assertEqual(expected_dial_position, actual_dial_position)

if __name__ == '__main__':
    unittest.main()