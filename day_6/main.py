from argparse import ArgumentError
import math

import puzzles


def transpose_problems(rows):
    columns = dict()
    for row in rows:
        for i, cell in enumerate(row.split()):
            if i not in columns:
                columns[i] = []
            columns[i].append(cell)
    return columns


def solve_problem(row):
    operand = row[-1:][0]
    values = map(int, row[:-1])

    match operand:
        case "+":
            return sum(values)
        case "*":
            return math.prod(values)
        case _:
            raise ArgumentError(row, "invalid row")


def run():
    problems = transpose_problems(puzzles.lines("day_6"))

    total = 0
    for i in problems:
        total += solve_problem(problems[i])
    print("The total is", total)


if __name__ == '__main__':
    run()
