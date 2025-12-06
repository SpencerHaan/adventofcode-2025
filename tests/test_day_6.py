import textwrap
import unittest

import day_6


class TestDay6(unittest.TestCase):
    def test_transpose_worksheet(self):
        worksheet = textwrap.dedent("""\
             51 64 
            387 23 
            215 314
            *   +  """)

        expected = textwrap.dedent("""\
              4 
            431 
            623+

            175 
            581 
             32*""")

        actual = day_6.transpose_worksheet(worksheet)

        self.assertEqual(expected, actual)

    def test_transcribe_problem(self):
        test_cases = [
            (textwrap.dedent("""\
              4 
            431 
            623+"""), "+", [4, 431, 623]),
            (textwrap.dedent("""\
            175 
            581 
             32*"""), "*", [175, 581, 32])
        ]
        for (problem, expected_operand, expected_values) in test_cases:
            with self.subTest(problem=problem, expected_operand=expected_operand, expected_values=expected_values):
                actual_operand, actual_values = day_6.transcribe_problem(problem)

                self.assertEqual(expected_operand, actual_operand)
                self.assertEqual(expected_values, actual_values)

    def test_solve_problem(self):
        test_cases = [
            (("+", [4, 431, 623]), 1058),
            (("*", [175, 581, 32]), 3253600),
            (("+", [8, 248, 369]), 625),
            (("*", [356, 24, 1]), 8544),
        ]
        for (operand, values), expected_result in test_cases:
            with self.subTest(test_case=(operand, values), expected_result=expected_result):
                actual_result = day_6.solve_problem(operand, values)

                self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
