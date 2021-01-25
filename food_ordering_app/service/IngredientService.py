"""
Service for Ingredients
"""
from food_ordering_app.model import Exception
from food_ordering_app.repo import IngredientRepo
import logging as LOG
from flask import abort

def get_ingredients():
    res = IngredientRepo.getAll()
    filtered_Ingredients = []
    for item in res:
        filtered_Ingredients.append(item.split(';')[0])
    return filtered_Ingredients


def ShoppingBag():
    try:
        res = IngredientRepo.shoppingBag()
        return res
    except BaseException as exc:
        LOG.error(exc)
        return abort(401, Exception.Connection_Error)
