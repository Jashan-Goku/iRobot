"""
Service for Ingredients
"""
import json
from food_ordering_app.repo import RecipeRepo, IngredientRepo
from food_ordering_app.model import Recipe, Exception
from flask import abort
import logging as LOG


def getRecipes(query):
    try:
        res = RecipeRepo.QueryRecipe(query)
        response = []
        res = json.loads(res.content)
        for item in res:
            response.append(Recipe.Details(id=item['id'],
                                           missedIngredients=item['missedIngredients'],
                                           missedIngredientCount=item['missedIngredientCount'],
                                           title=item['title'],
                                           unusedIngredients=item['unusedIngredients'],
                                           usedIngredients=item['usedIngredients']).to_dict())
        return response
    except BaseException as exc:
        LOG.error(exc)
        return abort(401, Exception.Connection_Error)


def SelectedRecipes(choice):
    try:
        res = RecipeRepo.selectRecipe(choice)
        response = []
        res = json.loads(res.content)
        for item in res['extendedIngredients']:
            response.append({"_id": item['id'],
                             'name': item['name'],
                             "aisle": item['aisle']})
        IngredientRepo.selectedIngredients(
            {"Recipe Name": res['title'], 'Ingredients': response, 'price': res['pricePerServing']})
        return "All the Ingredients are added to your shopping List for this recipe"
    except BaseException as exc:
        LOG.error(exc)
        return abort(401, Exception.Connection_Error)
