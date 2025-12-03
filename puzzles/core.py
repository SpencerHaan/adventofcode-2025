from pathlib import Path

def lines(day):
    input_file = Path.cwd().parent.joinpath(f"data/{day}.txt").open()
    try:
        for line in input_file:
            line = line.removesuffix("\n")
            line = line.strip()

            yield line
    finally:
        input_file.close()
