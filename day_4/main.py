import puzzles


def is_roll_accessible(grid, position):
    origin_x, origin_y = position

    adjacent_count = 0
    for y in range(origin_y - 1, origin_y + 2):
        if y < 0 or y >= grid.height:
            continue

        for x in range(origin_x - 1, origin_x + 2):
            if x < 0 or x >= grid.height or (y == origin_y and x == origin_x):
                continue

            if grid[x, y] == "@":
                adjacent_count += 1

    return adjacent_count < 4


def find_inaccessible_rolls(grid):
    inaccessible_rolls = []

    for position, cell in grid:
        if cell != "." and is_roll_accessible(grid, position):
            inaccessible_rolls.append(position)

    return inaccessible_rolls


def remove_rolls(grid):
    inaccessible_rolls = find_inaccessible_rolls(grid)

    inaccessible_rolls_count = len(inaccessible_rolls)
    if inaccessible_rolls_count == 0:
        return 0

    for position, cell in grid:
        if position in inaccessible_rolls:
            grid[position] = "."

    return remove_rolls(grid) + inaccessible_rolls_count


def run():
    grid = puzzles.grid("day_4")
    print(grid)

    inaccessible_rolls = find_inaccessible_rolls(grid)
    print("Inaccessible rolls:", len(inaccessible_rolls))
    print()

    removed_rolls = remove_rolls(grid)
    print(grid)
    print("Removed rolls:", removed_rolls)


if __name__ == '__main__':
    run()
