from .limit import Limit


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.__x_limit = Limit(x, range(y, y + height), x + width, range(y, y + height))
        self.__y_limit = Limit(y, range(x, x + width), y + height, range(x, x + width))

    def x_limit(self):
        return self.__x_limit

    def y_limit(self):
        return self.__y_limit

    @staticmethod
    def from_corners(a, b):
        x = a.x if a.x < b.x else b.x
        y = a.y if a.y < b.y else b.y
        width = abs(a.x - b.x)
        height = abs(a.y - b.y)
        return Rectangle(x, y, width, height)

    def calculate_area(self):
        return (self.width + 1) * (self.height + 1)
