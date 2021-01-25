"""
Repo for Ingredients
"""
from food_ordering_app.repo.Database import mongo
from food_ordering_app.model import ShoppingBag, Exception
import os
import logging as LOG
from flask import abort

Collection = mongo.db.ShoppingBag


def getAll():
    Ingredient = os.path.join(os.path.dirname(__file__), "list_of_ingredients")
    with open(Ingredient, "r") as content:
        response = content.read().splitlines()
    return response


def selectedIngredients(ingredients):
    try:
        found = Collection.find_one({"Recipe Name": ingredients['Recipe Name']})
        if found:
            return "Already have Item Added to the Bag"
        Collection.insert(ingredients)
        return "Item Added to your shopping bag"
    except BaseException as exc:
        LOG.error(exc)
        return abort(401, Exception.Connection_Error)



def shoppingBag():
    try:
        bag = []
        found = Collection.find()
        for item in found:
            bag.append(ShoppingBag.Bag(Recipe=item['Recipe Name'],
                                       Ingredients=item['Ingredients'],
                                       price=item['price']).to_dict())
        return bag
    except BaseException as exc:
        LOG.error(exc)
        return abort(401, Exception.Connection_Error)
