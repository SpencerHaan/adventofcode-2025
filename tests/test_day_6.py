import unittest

import day_6


TEST_INPUT = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  ",
]

class TestDay6(unittest.TestCase):
    def test_transpose_problems(self):
        expected = dict([
            (0, ['123', '45', '6', '*']),
            (1, ['328', '64', '98', '+']),
            (2, ['51', '387', '215', '*']),
            (3, ['64', '23', '314', '+']),
        ])

        actual = day_6.transpose_problems(TEST_INPUT)

        self.assertEqual(expected, actual)

    def test_solve_problem(self):
        test_cases = [
            (['123', '45', '6', '*'], 33210),
            (['328', '64', '98', '+'], 490),
            (['51', '387', '215', '*'], 4243455),
            (['64', '23', '314', '+'], 401),
        ]
        for problem, expected_result in test_cases:
            with self.subTest(test_case=problem, expected_result=expected_result):
                actual_result = day_6.solve_problem(problem)

                self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
