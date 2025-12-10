import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point2D(self.x * other.x, self.y * other.y)

    @staticmethod
    def zero():
        return Point2D(0, 0)

    def invert(self):
        return Point2D(self.y, self.x)

    def distance_to(self, other):
        x = math.pow(abs(self.x - other.x), 2)
        y = math.pow(abs(self.y - other.y), 2)
        return math.sqrt(x + y)

    def offset_towards(self, other, step=1):
        x_offset = min(max(-step, self.x - other.x), step)
        y_offset = min(max(-step, self.y - other.y), step)
        return Point2D(x_offset, y_offset)

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def distance_to(self, other):
        x = math.pow(abs(self.x - other.x), 2)
        y = math.pow(abs(self.y - other.y), 2)
        z = math.pow(abs(self.z - other.z), 2)
        return math.sqrt(x + y + z)
