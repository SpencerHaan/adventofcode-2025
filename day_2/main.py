from pathlib import Path

def find_place_value_divisors(n):
    if n == 1:
        return [1]

    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    return sorted(divisors)

def find_invalid_ids(lower, upper):
    lower_pv = len(str(lower))
    upper_pv = len(str(upper))

    if lower_pv != upper_pv:
        threshold = pow(10, lower_pv)

        lower_invalid_ids = find_invalid_ids(lower, threshold - 1)
        upper_invalid_ids = find_invalid_ids(threshold, upper)

        return lower_invalid_ids + upper_invalid_ids
    elif lower_pv < 2:
        return []
    else:
        invalid_ids = set()
        candidate_ids = range(lower, upper + 1)

        for divisor in find_place_value_divisors(lower_pv):
            lower_left = str(lower)[:divisor]
            upper_left = str(upper)[:divisor]

            for v in range(int(lower_left), int(upper_left) + 1):
                candidate_id = int(str(v) * int(lower_pv / divisor))
                if candidate_id in candidate_ids:
                    invalid_ids.add(candidate_id)

    return list(invalid_ids)

def run():
    input_file = Path.cwd().parent.joinpath("data/day_2.txt").open()

    invalid_ids_sum = 0
    try:
        for input_range in input_file.read().split(","):
            lower, upper = input_range.split("-")

            invalid_ids = find_invalid_ids(int(lower), int(upper))

            if len(invalid_ids):
                print(input_range, "has invalid IDs,", sorted(invalid_ids))
            else:
                print(input_range, "contains no invalid IDs")

            invalid_ids_sum += sum(invalid_ids)

    finally:
        input_file.close()

    print("The sum of the IDs is", invalid_ids_sum)

if __name__ == '__main__':
    run()