import sys
import time

import puzzles

from day_9.polygon import Polygon
from day_9.rectangle import Rectangle
from day_9.vertex import Vertex


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
    min_x = sys.maxsize
    max_x = 0
    min_y = sys.maxsize
    max_y = 0

    red_tiles = []
    for line in puzzles.lines("day_9"):
        x, y = line.split(",")

        x = int(x)
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

        y = int(y)
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

        red_tiles.append(Vertex(x, y))

    polygon = Polygon.from_points(red_tiles)

    cache = dict()
    rectangles = []
    start_time = time.time()
    for i, a in enumerate(red_tiles):
        for b in red_tiles[i + 1:]:
            c = Vertex(b.x, a.y)
            d = Vertex(a.x, b.y)

            if c not in cache:
                cache[c] = c not in polygon
            if d not in cache:
                cache[d] = d not in polygon

            if cache[c] or cache[d]:
                continue

            rectangle = Rectangle.from_corners(a, b)
            rectangles.append(rectangle)

    end_time = time.time()
    print(f"Took {end_time - start_time} seconds to calculate areas")
    start_time = time.time()

    rectangle = None
    for rectangle in sorted(rectangles, key=lambda r: -r.calculate_area()):
        if not polygon.intersects(rectangle):
            break
    end_time = time.time()
    print(f"Took {end_time - start_time} seconds to find the largest area")

    print(f"The largest area is: {rectangle.calculate_area()}")


if __name__ == '__main__':
    run()
