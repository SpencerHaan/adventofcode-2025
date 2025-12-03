from pathlib import Path

def lines(day):
    for pf in puzzle_file(day):
        for line in pf:
            line = line.removesuffix("\n")
            line = line.strip()

            yield line

def delimited(day, delimiter = ","):
    for pf in puzzle_file(day):
        for part in pf.read().split(delimiter):
            yield part

def puzzle_file(day):
    file = Path.cwd().parent.joinpath(f"data/{day}.txt").open()
    try:
        yield file
    finally:
        file.close()
