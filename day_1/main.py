from pathlib import Path

class Safe:
    def __init__(self, dial_position):
        self.__current_dial_position = dial_position

    def rotate_dial(self, instruction):
        rotation, *rest = instruction
        distance = int("".join(rest))

        zero_clicks = int(distance / 100)
        distance = distance % 100

        if distance != 0:
            if rotation == "L":
                next_dial_position = self.__current_dial_position - distance
            else:
                next_dial_position = self.__current_dial_position + distance

            if next_dial_position < 0:
                next_dial_position += 100
            elif next_dial_position > 99:
                next_dial_position -= 100

            if (
                    next_dial_position == 0
                    or (rotation == "L" and next_dial_position > self.__current_dial_position != 0)
                    or (rotation == "R" and next_dial_position < self.__current_dial_position)
            ):
                zero_clicks += 1

            self.__current_dial_position = next_dial_position

        return zero_clicks

    def dial_position(self):
        return self.__current_dial_position

def run():
    password = 0

    safe = Safe(50)
    input_file = Path.cwd().parent.joinpath("data/day_1.txt").open()

    print(f"The dial starts by pointing at {safe.dial_position()}")
    try:
        for instruction in input_file:
            instruction = instruction.removesuffix("\n")
            instruction = instruction.strip()

            zero_clicks = safe.rotate_dial(instruction)

            if zero_clicks != 0:
                print(f"The dial is rotated {instruction} to point at {safe.dial_position()}, zero clicks {zero_clicks}")
            else:
                print(f"The dial is rotated {instruction} to point at {safe.dial_position()}")

            password += zero_clicks

        print(f"The password is: {password}")
    finally:
        input_file.close()

if __name__ == '__main__':
    run()