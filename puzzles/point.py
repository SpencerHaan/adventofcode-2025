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
