import puzzles


def find_largest_joltage(battery_bank):
    largest_battery_start = 0
    largest_battery_start_index = 0
    for i, battery in enumerate(battery_bank[:-1]):
        if largest_battery_start < int(battery):
            largest_battery_start = int(battery)
            largest_battery_start_index = i

    largest_battery_end = 0
    for battery in battery_bank[largest_battery_start_index+1:]:
        if largest_battery_end < int(battery):
            largest_battery_end = int(battery)

    return largest_battery_start * 10 + largest_battery_end

def run():
    total_joltage_output = 0
    for battery_bank in puzzles.lines("day_3"):
        total_joltage_output += find_largest_joltage(battery_bank)

    print("The total joltage output is", total_joltage_output)

if __name__ == '__main__':
    run()
