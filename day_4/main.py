import puzzles


def is_roll_accessible(grid, position, bounds):
    x, y = position
    w, h = bounds

    adjacent_count = 0
    for r in range(y - 1, y + 2):
        if r < 0 or r >= h:
            continue

        for c in range(x - 1, x + 2):
            if c < 0 or c >= w or (r == y and c == x):
                continue

            if grid[r][c] == "@":
                adjacent_count += 1

    return adjacent_count < 4


def find_inaccessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])

    inaccessible_rolls = []

    for row in range(0, rows):
        for col in range(0, cols):
            if grid[row][col] == ".":
                continue

            if is_roll_accessible(grid, (col, row), (cols, rows)):
                inaccessible_rolls.append((col, row))

    return inaccessible_rolls


def run():
    blob = puzzles.blob("day_4")
    grid = blob.split("\n")

    inaccessible_rolls = find_inaccessible_rolls(grid)
    print("Inaccessible rolls:", len(inaccessible_rolls))


if __name__ == '__main__':
    run()
