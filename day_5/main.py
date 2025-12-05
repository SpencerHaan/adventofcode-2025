import puzzles

class IngredientDb:
    def __init__(self, ingredients_ranges):
        self.ingredient_ranges = ingredients_ranges

    def __str__(self):
        string = ""
        for ingredient_range in self.ingredient_ranges:
            string += f"{ingredient_range.start}-{ingredient_range.stop}\n"

        return string

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
        for ingredient_range in self.ingredient_ranges:
            if ingredient in ingredient_range:
                return True
        return False


def run():
    id_ranges, available_ids = puzzles.chunks("day_5")

    db = IngredientDb.parse(id_ranges.blob())
    available_ingredients = map(int, available_ids.lines())

    fresh_ingredients = []
    for available_ingredient in available_ingredients:
        if db.is_fresh(available_ingredient):
            fresh_ingredients.append(available_ingredient)

    print(f"There is {len(fresh_ingredients)} fresh ingredients")


if __name__ == '__main__':
    run()
