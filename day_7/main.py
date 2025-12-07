from argparse import ArgumentError

import puzzles


def split_beam(point):
    x, y = point
    return [
        (x - 1, y),
        (x + 1, y)
    ]


def analyze_manifold(diagram):
    beam_x = None
    start_y = None
    for point, cell in diagram:
        if cell == "S":
            beam_x, start_y = point
            break

    if beam_x is None or start_y is None:
        raise ArgumentError(diagram, "No entry point found")

    split_counter = 0
    beams = {(beam_x, start_y)}
    for y in range(start_y, diagram.height):
        new_beams = set()
        for beam_x, _ in beams:
            beam = (beam_x, y)
            if diagram[beam] == "^":
                new_beams.update(split_beam(beam))
                split_counter += 1
            else:
                new_beams.add(beam)
        beams = new_beams

    return split_counter


def run():
    diagram = puzzles.grid("day_7")

    total_splits = analyze_manifold(diagram)

    print(f"Tachyon beam is split a total of {total_splits} times")



if __name__ == "__main__":
    run()
