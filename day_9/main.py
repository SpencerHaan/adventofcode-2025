import puzzles
from puzzles import Point2D


def calculate_area(a, b):
    width = abs(a.x - b.x) + 1
    height = abs(a.y - b.y) + 1
    return width * height


def find_largest_area(points):
    largest_area = 0
    for i, a in enumerate(points):
        for b in points[i + 1 :]:
            area = calculate_area(a, b)
            if area > largest_area:
                largest_area = area
    return largest_area


def run():
    red_tiles = []
    for line in puzzles.lines("day_9"):
        x, y = line.split(",")
        red_tiles.append(Point2D(int(x), int(y)))

    largest_area = find_largest_area(red_tiles)

    print(f"The largest area is: {largest_area}")


if __name__ == '__main__':
    run()
