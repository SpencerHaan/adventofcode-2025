from puzzles import Point2D


class Vertex(Point2D):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__prev = None
        self.__next = None
        self.__direction = None

    def __iter__(self):
        current_vertex = self
        while True:
            yield current_vertex
            current_vertex = current_vertex.__next
            if current_vertex is None or current_vertex == self:
                break

    def next(self):
        return self.__next

    def prev(self):
        return self.__prev

    def direction(self):
        return self.__direction

    def link_next(self, other):
        other.__prev = self
        self.__next = other
        self.__direction = self.offset_towards(other)
