from enum import Enum
from unittest import case

Orientation = Enum("Orientation", ["Horizontal", "Vertical"])

class Line:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        return f"{str(self.__a)} - {self.__b}"

    def x_range(self):
        x_a = self.__a.x
        x_b = self.__b.x
        if x_a > x_b:
            x_a -= 1
        else:
            x_b += 1
        return range(x_a, x_b)

    def y_range(self):
        y_a = self.__a.y
        y_b = self.__b.y
        if y_a > y_b:
            y_a -= 1
        else:
            y_b += 1
        return range(y_a, y_b)

    def is_intersecting(self, other):
        if self.is_horizontal():
            return other.is_vertical() and other.__a.y in self.y_range() and self.__a.x in other.x_range()
        elif self.is_vertical():
            return other.is_horizontal() and other.__a.x in self.x_range() and self.__a.y in other.y_range()
        return False

    def orientation(self):
        if self.is_horizontal():
            return Orientation.Horizontal
        elif self.is_vertical():
            return Orientation.Vertical
        else:
            raise NotImplementedError

    def is_horizontal(self):
        return self.__a.x == self.__b.x

    def is_vertical(self):
        return self.__a.y == self.__b.y

    def length(self):
        return self.__a.distance_to(self.__b)
