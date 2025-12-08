class Node:
    def __init__(self, value):
        self.__value = value
        self.__parent = None
        self.__children = set()

    def __str__(self):
        return str(self.__value)

    def __eq__(self, other):
        return self.__value == other.__value

    def __hash__(self):
        return hash(self.__value)

    def __iter__(self):
        return iter(self.__children)

    def get_value(self):
        return self.__value

    def get_root(self):
        if self.__parent is None:
            return self
        return self.__parent.get_root()

    def add_child(self, child):
        child.__parent = self
        self.__children.add(child)
