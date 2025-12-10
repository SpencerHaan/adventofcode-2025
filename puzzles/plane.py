from .point import Point2D


class Plane:
    def __init__(self, width, height, origin = Point2D(0, 0)):
        self.__width = width
        self.__height = height
        self.__origin = origin
        self.__items = dict()

    def __getitem__(self, point):
        if point in self.__items:
            return self.__items[point]
        elif point in self:
            return None
        else:
            raise KeyError(f"{point} is out of bounds")

    def __setitem__(self, point, item):
        if point in self:
            self.__items[point] = item
        else:
            raise KeyError(f"{point} is out of bounds")

    def __contains__(self, point):
        return (
                self.__origin.x <= point.x < self.__origin.x + self.__width
                and self.__origin.y <= point.y < self.__origin.y + self.__height
        )

    def __iter__(self):
        for y in range(self.__origin.y, self.__height):
            for x in range(self.__origin.x, self.__width):
                point = Point2D(x, y)
                yield point, self[Point2D(x, y)]

    def __str__(self):
        return f"{{w={self.__width} h={self.__height} o={self.__origin}]}}"


    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def rendered_string(self, fill =" "):
        string = ""
        current_y = self.__origin.y
        for point, item in self:
            if point.y != current_y:
                string += "\n"
                current_y = point.y

            if item is not None:
                string += str(item)
            else:
                string += fill

        return string

    @staticmethod
    def from_string(string):
        lines = string.removesuffix("\n").split("\n")

        height = len(lines)
        if height == 0:
            raise ValueError("Grid is empty")
        width = len(lines[0])

        plane = Plane(width, height)

        for row, line in enumerate(lines):
            if len(line) != width:
                raise ValueError(f"Non-uniform width: expected {width}, got {len(line)}")

            for col, cell in enumerate(line):
                plane[Point2D(row, col)] = cell
