import functools

import puzzles

class BitSet:
    def __init__(self, value: int, length: int = 0):
        self.__value = value
        self.__length = length

    def __str__(self):
        return format(self.__value, f"#0{self.__length + 2}b")

    def __eq__(self, other):
        if isinstance(other, int):
            return self.__value == other
        return self.__value == other.__value

    def __xor__(self, other):
        return BitSet(self.__value ^ other.__value, length=self.__length)

    def length(self):
        return self.__length

BitSet.ZERO = BitSet(0)


class ManualEntry:
    def __init__(self, diagram, buttons, joltage_requirements):
        self.__diagram = diagram
        self.__buttons = buttons
        self.__joltage_requirements = joltage_requirements

    @staticmethod
    def from_binary(diagram, buttons, joltage_requirements = None):
        diagram = BitSet(diagram)
        buttons = list(map(lambda b: BitSet(b, diagram.length()), buttons))
        return ManualEntry(diagram, buttons, joltage_requirements)

    def diagram(self):
        return self.__diagram

    def buttons(self):
        return self.__buttons


def parse_diagram(string):
    translated = string[1:-1].replace(".", "0").replace("#", "1")
    return BitSet(int(translated, 2), len(translated))


def parse_buttons(strings, diagram_size):
    buttons = []
    for button in strings:
        affected_bits = 0b0
        for light in button[1:-1].split(","):
            reversed_base_10 = pow(10, diagram_size - int(light) - 1) # lights are interpreted left to right
            affected_bits |= int(str(reversed_base_10), 2)
        buttons.append(BitSet(affected_bits, diagram_size))
    return buttons


def collect_valid_button_presses(manual_entry, found_presses, current_presses = None, offset = 0):
    if current_presses is None:
        current_presses = []

    for i, button in enumerate(manual_entry.buttons()[offset:]):
        next_presses = current_presses + [button]

        collect_valid_button_presses(manual_entry, found_presses, next_presses, offset + i + 1)

        lights_state = functools.reduce(lambda a, b: a ^ b, next_presses, BitSet.ZERO)
        if lights_state == manual_entry.diagram():
            found_presses.append(next_presses)


def find_fewest_button_presses(manual_entry):
    found_presses = []
    collect_valid_button_presses(manual_entry, found_presses)

    if len(found_presses) == 0:
        return 0

    button_press_lengths = map(lambda s: len(s), found_presses)
    return sorted(button_press_lengths)[0]


def run():
    total_presses = 0
    for line in puzzles.lines("day_10"):
        parts = line.split()

        diagram = parse_diagram(parts[0])
        buttons = parse_buttons(parts[1:-1], diagram.length())
        # joltage_requirements = parts[-1] # Not needed yet

        manual_entry = ManualEntry(diagram, buttons, None)

        total_presses += find_fewest_button_presses(manual_entry)

    print(f"Total fewest presses: {total_presses}")


if "__main__" == __name__:
    run()
