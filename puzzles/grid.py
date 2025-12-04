class Grid:
    def __init__(self, points, width, height):
        self.points = points
        self.width = width
        self.height = height

    def __getitem__(self, position):
        x, y = position
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise KeyError(f"{position} is out of bounds")
        return self.points[x, y]

    def __setitem__(self, position, value):
        x, y = position
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise KeyError(f"{position} is out of bounds")
        self.points[x, y] = value

    def __iter__(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                position = (x, y)
                if position in self.points:
                    yield position, self.points[position]
                else:
                    yield None

    def __str__(self):
        string = ""
        current_width = 0
        for (x, y), cell in self:
            if cell is None:
                string += " "
            else:
                string += str(cell)

            current_width += 1
            if current_width == self.width:
                string += "\n"
                current_width = 0

        return string

    @staticmethod
    def from_string(string):
        lines = string.removesuffix("\n").split("\n")

        height = len(lines)
        if height == 0:
            raise ValueError("Grid is empty")
        width = len(lines[0])

        points = dict()
        for row, line in enumerate(lines):
            if len(line) != width:
                raise ValueError(f"Non-uniform width: expected {width}, got {len(line)}")

            for col, cell in enumerate(line):
                points[col, row] = cell

        return Grid(points, width, height)
