class Limit:
    def __init__(self, min_p, min_n_range: range, max_p, max_n_range: range):
        self.__min_p = min_p
        self.__min_n_range = min_n_range
        self.__max_p = max_p
        self.__max_n_range = max_n_range

    def __contains__(self, point):
        a, b = point
        if a < self.__min_p or (a == self.__min_p and b not in self.__min_n_range):
            return False
        if a > self.__max_p or (a == self.__max_p and b not in self.__max_n_range):
            return False
        return True

    def p(self):
        return self.__min_p, self.__max_p
