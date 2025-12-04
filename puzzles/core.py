from contextlib import contextmanager
from pathlib import Path


def blob(day):
    with puzzle_file(day) as pf:
        return pf.read().removesuffix("\n")


def lines(day):
    with puzzle_file(day) as pf:
        for line in pf:
            line = line.removesuffix("\n")
            line = line.strip()

            yield line


def delimited(day, delimiter=","):
    with puzzle_file(day) as pf:
        for part in pf.read().split(delimiter):
            yield part


@contextmanager
def puzzle_file(day):
    file = Path.cwd().parent.joinpath(f"data/{day}.txt").open()
    try:
        yield file
    finally:
        file.close()
