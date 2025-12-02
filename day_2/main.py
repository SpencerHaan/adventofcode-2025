from pathlib import Path

def find_invalid_ids(lower, upper):
    invalid_ids = []

    lower_str = str(lower)
    if len(lower_str) % 2 != 0:
        lower_str = "1" + "0" * len(lower_str)
        lower = int(lower_str)

    upper_str = str(upper)
    if len(upper_str) % 2 != 0:
        upper_str = "9" * (len(upper_str) - 1)
        upper = int(upper_str)

    if lower > upper:
        return invalid_ids

    lower_left_half = lower_str[:len(lower_str)//2]
    upper_left_half = upper_str[:len(upper_str)//2]

    id_candidates = range(lower, upper + 1)

    for id_half in range(int(lower_left_half), int(upper_left_half) + 1):
        suspected_id = int(str(id_half) * 2)
        if suspected_id in id_candidates:
            invalid_ids.append(suspected_id)

    return invalid_ids

def run():
    input_file = Path.cwd().parent.joinpath("data/day_2.txt").open()

    invalid_ids_sum = 0
    try:
        for input_range in input_file.read().split(","):
            lower, upper = input_range.split("-")

            invalid_ids = find_invalid_ids(int(lower), int(upper))

            if len(invalid_ids):
                print(input_range, "has invalid IDs,", invalid_ids)
            else:
                print(input_range, "contains no invalid IDs")

            invalid_ids_sum += sum(invalid_ids)

    finally:
        input_file.close()

    print("The sum of the IDs is", invalid_ids_sum)

if __name__ == '__main__':
    run()