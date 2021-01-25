"""
Repo for Recipe
"""

import requests
import os
import logging as LOG
from flask import abort
from food_ordering_app.model import Exception


def QueryRecipe(query):
    try:
        res = requests.get(
            os.getenv('baseUrl') + "recipes/findByIngredients?ingredients=" + query + "&number=20&apiKey=" + os.getenv(
                'apiKey'))
        return res
    except Exception as exc:
        LOG.error(exc)
        return abort(401, Exception.Connection_Error)


def selectRecipe(choice):
    res = requests.get(
        os.getenv('baseUrl') + "recipes/{id}/information?includeNutrition=false&apiKey=".format(id=choice) + os.getenv(
            'apiKey'))
    return res