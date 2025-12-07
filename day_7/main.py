from argparse import ArgumentError

import puzzles


def find_entry_point(diagram):
    entry_point = None
    for point, cell in diagram:
        if cell == "S":
            entry_point = point
            break

    if entry_point is None:
        raise ArgumentError(diagram, "No entry point found")

    return entry_point


def split_beam(point):
    x, y = point
    return [
        (x - 1, y),
        (x + 1, y)
    ]


def analyze_manifold(diagram, from_point, forks):
    x, y = from_point
    y += 1

    to_point = (x, y)
    if y == diagram.height:
        return 1
    elif to_point in forks:
        return forks[to_point]
    elif diagram[x, y] == "^":
        total_timelines = 0
        for next_point in split_beam(to_point):
            timelines = analyze_manifold(diagram, next_point, forks)
            forks[next_point] = timelines
            total_timelines += timelines
        return total_timelines
    else:
        timelines = analyze_manifold(diagram, to_point, forks)
        forks[to_point] = timelines
        return timelines


def run():
    diagram = puzzles.grid("day_7")

    entry_point = find_entry_point(diagram)
    total_splits = analyze_manifold(diagram, entry_point, dict())

    print(f"Tachyon beam is split a total of {total_splits} times")



if __name__ == "__main__":
    run()
