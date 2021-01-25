"""
Initialization of Recipe return response
"""


class Details:

    def __init__(self, id=None, missedIngredientCount=None, missedIngredients=None, title=None, unusedIngredients=None,
                 usedIngredients=None):
        self.id = id
        self.missedIngredientCount = missedIngredientCount
        self.missedIngredients = missedIngredients
        self.title = title
        self.unusedIngredients = unusedIngredients
        self.usedIngredients = usedIngredients

    def to_dict(self):
        json_map = {
            'id': self.id,
            'missedIngredientCount': self.missedIngredientCount,
            'missedIngredients': self.missedIngredients,
            'title': self.title,
            'unusedIngredients': self.unusedIngredients,
            'usedIngredients': self.usedIngredients

        }
        return json_map
