import sys
import os
from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from flask_cors import CORS
from food_ordering_app.service import IngredientService
from food_ordering_app.service import RecipeService

APP = Flask(__name__)
api = Api(APP, title="iRobot Food Ordering Project")
CORS(APP)
sys.path.insert(0, '')


@api.route('/basic')
class Setup(Resource):
    """
    This is to check application is up or not
    """
    def get(self):
        response = "Application is working"
        return response


@api.route('/ingredients')
class Ingredients(Resource):
    """
    This is to get all the list of available ingredients
    """
    def get(self):
        response = IngredientService.get_ingredients()
        return response


@api.route('/recipe')
@api.doc(params={'Ingredients': {'description': 'Name of ingredient', 'required': True}})
class GetRecipe(Resource):
    """
    This is to get recipe on the basis of Ingredients in shopping bag
    """
    def get(self):
        query = request.args.get('Ingredients')
        response = RecipeService.getRecipes(query)
        return response


@api.route('/choice')
@api.doc(params={'choice': {'description': 'Please type the recipe id you like', 'type': int, 'required': True}})
class SelectedRecipe(Resource):
    """
    This is to select the recipe
    """
    def post(self):
        choice = request.args.get('choice')
        import sys
        print(choice, file=sys.stderr)
        response = RecipeService.SelectedRecipes(choice)
        return response


@api.route('/ShoppingBag')
class ShoppingBag(Resource):
    """
    This is to get the shopping Bag
    """
    def get(self):
        response = IngredientService.ShoppingBag()
        return jsonify({"Shopping Bag": response})


if __name__ == '__main__':
    APP.run()
