import unittest

from day_10.main import ManualEntry, find_fewest_button_presses


class Day10Test(unittest.TestCase):
    def test_find_fewest_button_presses(self):
        test_cases = [
            (ManualEntry.from_binary(diagram=0b0110, buttons=[0b0001, 0b0101, 0b0010, 0b0011, 0b1010, 0b1100]), 2),
            (ManualEntry.from_binary(diagram=0b00010, buttons=[0b10111, 0b00110, 0b10001, 0b11100, 0b01111]), 3),
            (ManualEntry.from_binary(diagram=0b011101, buttons=[0b111110, 0b100110, 0b111011, 0b011000]), 2),
        ]
        for (manual_entry, expected_presses) in test_cases:
            with self.subTest(test_case=manual_entry, expected_presses=expected_presses):
                actual_presses = find_fewest_button_presses(manual_entry)

                self.assertEqual(expected_presses, actual_presses)
