import puzzles

def find_largest_battery(battery_bank):
    index = 0
    largest_battery = 0

    for i, b in enumerate(battery_bank):
        battery = int(b)
        if battery > largest_battery:
            index = i
            largest_battery = battery

    return index, largest_battery

def find_largest_joltage(battery_bank, max_battery_count = 2):
    selected_batteries = []
    battery_bank_length = len(battery_bank)

    end_index = battery_bank_length
    while max_battery_count > 0:
        index, largest = find_largest_battery(battery_bank[:end_index])

        if index + max_battery_count > len(battery_bank):
            end_index = index
            continue

        selected_batteries.append(largest)
        max_battery_count -= 1
        battery_bank = battery_bank[index + 1:]

        end_index = battery_bank_length

    return int("".join(map(str, selected_batteries)))

def run():
    total_joltage_output = 0
    for battery_bank in puzzles.lines("day_3"):
        total_joltage_output += find_largest_joltage(battery_bank, 12)

    print("The total joltage output is", total_joltage_output)

if __name__ == '__main__':
    run()
