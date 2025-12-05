import puzzles

def compress_ranges(ranges):
    compressed_ranges = []
    current_range = None
    for r in sorted(ranges, key=lambda _r: _r.start):
        if current_range is None:
            current_range = r
            continue
        if r.start <= current_range.stop:
            current_range = range(
                current_range.start,
                current_range.stop if current_range.stop > r.stop else r.stop
            )
        else:
            compressed_ranges.append(current_range)
            current_range = r
    compressed_ranges.append(current_range)

    return compressed_ranges


class IngredientDb:
    def __init__(self, ingredients_ranges):
        self.__ingredient_ranges = compress_ranges(ingredients_ranges)

    def __str__(self):
        string = ""
        for ingredient_range in self.__ingredient_ranges:
            string += f"{ingredient_range.start}-{ingredient_range.stop}\n"
        return string

    def ranges(self):
        return self.__ingredient_ranges

    @staticmethod
    def parse(string):
        ingredient_ranges = []
        for line in string.split("\n"):
            start, *end = line.split("-")

            start = int(start)
            end = int("".join(end)) + 1
            ingredient_ranges.append(range(start, end))
        return IngredientDb(ingredient_ranges)

    def is_fresh(self, ingredient):
        for ingredient_range in self.__ingredient_ranges:
            if ingredient in ingredient_range:
                return True
        return False

    def considered_fresh(self):
        total_fresh_ingredients = 0
        for compressed_range in self.__ingredient_ranges:
            total_fresh_ingredients += compressed_range.stop - compressed_range.start
        return total_fresh_ingredients


def run():
    id_ranges, available_ids = puzzles.chunks("day_5")

    db = IngredientDb.parse(id_ranges.blob())
    available_ingredients = map(int, available_ids.lines())

    fresh_ingredients = []
    for available_ingredient in available_ingredients:
        if db.is_fresh(available_ingredient):
            fresh_ingredients.append(available_ingredient)

    print(f"There is {len(fresh_ingredients)} fresh ingredients")
    print(f"There are {db.considered_fresh()} ingredients considered fresh")

if __name__ == '__main__':
    run()
