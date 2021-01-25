"""
Initialization of Shopping Bag return response
"""


class Bag:

    def __init__(self, Recipe=None, Ingredients=None, price=None):
        self.Recipe = Recipe
        self.Ingredients = Ingredients
        self.price = price

    def to_dict(self):
        json_map = {
            'Ingredients': self.Ingredients,
            'Average price per Recipe': self.price,
            'Recipe Name': self.Recipe
        }
        return json_map
