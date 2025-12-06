from argparse import ArgumentError
import math

import puzzles


def transpose_worksheet(worksheet):
    columns = dict()
    for row in worksheet.splitlines():
        for i, cell in enumerate(reversed(row)):
            if i not in columns:
                columns[i] = []
            columns[i].append(cell)

    worksheet = ""
    for i in columns:
        line = "".join(columns[i])
        if line.strip() == "":
            worksheet += "\n"
            continue

        worksheet += line

        if i != len(columns) - 1:
            worksheet += "\n"

    return worksheet


def transcribe_problem(problem):
    operand = ""
    values = []
    for row in problem.split("\n"):
        if operand == "":
            operand = row[-1:][0].strip()

        value = row[:-1]
        values.append(int(value))

    return operand, values


def solve_problem(operand, values):
    match operand:
        case "+":
            return sum(values)
        case "*":
            return math.prod(values)
        case _:
            raise ArgumentError(operand, "invalid operand")


def run():
    worksheet = transpose_worksheet(puzzles.blob("day_6"))

    problems = []
    for problem in worksheet.split("\n\n"):
        problems.append(transcribe_problem(problem))

    total = 0
    for operand, values in problems:
        total += solve_problem(operand, values)
    print("The total is", total)


if __name__ == '__main__':
    run()
