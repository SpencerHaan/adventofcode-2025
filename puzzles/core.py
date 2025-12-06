from contextlib import contextmanager
from pathlib import Path

from .grid import Grid


class InputProcessor:
    def __init__(self, string):
        self.__string = string

    def __str__(self):
        return self.__string

    def blob(self):
        return self.__string

    def lines(self):
        for line in self.__string.split("\n"):
            line = line.removesuffix("\n")
            line = line.strip()

            yield line

    def delimited(self, delimiter = ","):
        for part in self.__string.split(delimiter):
            yield part


def blob(day):
    with puzzle_file(day) as pf:
        return pf.read().removesuffix("\n")


def lines(day, strip = True):
    with puzzle_file(day) as pf:
        for line in pf:
            line = line.removesuffix("\n")
            if strip:
                line = line.strip()

            yield line


def delimited(day, delimiter=","):
    with puzzle_file(day) as pf:
        return InputProcessor(pf.read()).delimited(delimiter)

def chunks(day, delimiter="\n\n"):
    with puzzle_file(day) as pf:
        for part in InputProcessor(pf.read()).delimited(delimiter):
            yield InputProcessor(part.removesuffix("\n"))

def grid(day):
    with puzzle_file(day) as pf:
        return Grid.from_string(pf.read())


@contextmanager
def puzzle_file(day):
    file = Path.cwd().parent.joinpath(f"data/{day}.txt").open()
    try:
        yield file
    finally:
        file.close()
