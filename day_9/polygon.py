from puzzles import Point2D

from .limit import Limit
from .vertex import Vertex

RIGHT = Point2D(1, 0)
LEFT = Point2D(-1, 0)
UP = Point2D(0, -1)
DOWN = Point2D(0, 1)

# What have I done...?
class Polygon:
    def __init__(self, start: Vertex):
        self.__start = start

        self.__x_idx = dict()
        self.__x_table = list()
        self.__y_idx = dict()
        self.__y_table = list()

        vertices = list(start)

        next_x_i = 0
        for vertex in sorted(vertices, key=lambda v: v.x):
            x = vertex.x
            if x not in self.__x_idx:
                self.__x_idx[x] = next_x_i
                self.__x_table.append([])
                next_x_i += 1

            x_i = self.__x_idx[x]
            self.__x_table[x_i].append(vertex)

        next_y_i = 0
        for vertex in sorted(vertices, key=lambda v: v.y):
            y = vertex.y
            if y not in self.__y_idx:
                self.__y_idx[y] = next_y_i
                self.__y_table.append([])
                next_y_i += 1

            y_i = self.__y_idx[y]
            self.__y_table[y_i].append(vertex)

        x_min = self.__x_table[0]
        x_min_y_min = min(x_min, key=lambda v: v.y)
        x_min_y_max = max(x_min, key=lambda v: v.y)
        x_max = self.__x_table[-1]
        x_max_y_min = min(x_max, key=lambda v: v.y)
        x_max_y_max = max(x_max, key=lambda v: v.y)
        self.__x_limit = Limit(x_min_y_min.x, range(x_min_y_max.y, x_min_y_max.y + 1), x_max_y_min.x, range(x_max_y_max.y, x_max_y_max.y + 1))

        y_min = self.__y_table[0]
        y_min_x_min = min(y_min, key=lambda p: p.x)
        y_min_x_max = max(y_min, key=lambda p: p.x)
        y_max = self.__y_table[-1]
        y_max_x_min = min(y_max, key=lambda p: p.x)
        y_max_x_max = max(y_max, key=lambda p: p.x)
        self.__y_limit = Limit(y_min_x_min.y, range(y_min_x_min.x, y_min_x_max.x + 1), y_max_x_min.y, range(y_max_x_min.x, y_max_x_max.x + 1))

    def __iter__(self):
        return iter(self.__start)

    def __contains__(self, point):
        return (point.x, point.y) in self.__x_limit and (point.y, point.x) in self.__y_limit

    def intersects(self, other):
        min_x, max_x = other.x_limit().p()
        min_y, max_y = other.y_limit().p()

        y_points_by_x = self.__x_table[self.__x_idx[min_x]+1:self.__x_idx[max_x]]
        for y_points in y_points_by_x:
            for y_point in y_points:
                if y_point.y <= min_y:
                    v_next = y_point.next()
                    v_prev = y_point.prev()
                    if (v_prev.direction() == UP and v_prev.y > min_y) or (
                            v_next.direction() == DOWN and v_next.y > min_y):
                        return True
                elif y_point.y >= max_y:
                    v_next = y_point.next()
                    v_prev = y_point.prev()
                    if (v_prev.direction() == DOWN and v_prev.y < max_y) or (
                            v_next.direction() == UP and v_next.y < max_y):
                        return True

        x_points_by_y = self.__y_table[self.__y_idx[min_y]+1:self.__y_idx[max_y]]
        for x_points in x_points_by_y:
            for x_point in x_points:
                if x_point.x <= min_x:
                    v_next = x_point.next()
                    v_prev = x_point.prev()
                    if (v_prev.direction() == LEFT and v_prev.x > min_x) or (
                            v_next.direction() == RIGHT and v_next.x > min_x):
                        return True
                elif x_point.x >= max_x:
                    v_next = x_point.next()
                    v_prev = x_point.prev()
                    if (v_prev.direction() == RIGHT and v_prev.x < max_x) or (
                            v_next.direction() == LEFT and v_next.x < max_x):
                        return True

        return False

    @staticmethod
    def from_points(points):
        start = points[0]
        current = start
        for p in points[1:]:
            next_vertex = p

            current.link_next(next_vertex)
            current = next_vertex
        current.link_next(start)
        return Polygon(start)
