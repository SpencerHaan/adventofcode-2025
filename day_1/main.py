from pathlib import Path

BASE_DIR = Path.cwd().parent

dial_position = 50
password = 0

print(BASE_DIR)

input_file = BASE_DIR.joinpath("data/day_1.txt")

print(f"The dial starts by pointing at {dial_position}")
for line in input_file.open():
    line = line.removesuffix("\n")
    line = line.strip()

    rotation, *rest = line
    distance = int("".join(rest)) % 100

    if rotation == "L":
        dial_position -= distance
    else:
        dial_position += distance

    if dial_position < 0:
        dial_position = dial_position + 100
    elif dial_position > 99:
        dial_position = dial_position - 100

    if dial_position == 0:
        password += 1

    print(f"The dial is rotated {line} to point at {dial_position}")

print(f"\nThe password is {password}")
