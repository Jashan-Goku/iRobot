import unittest
from food_ordering_app.service import IngredientService, RecipeService
from food_ordering_app.repo import IngredientRepo, RecipeRepo
from food_ordering_app.repo.Database import mongo
import json

Collection = mongo.db.ShoppingBag


def data_remove_test():
    """
    Deleting Existing Data for Testing
    """
    Collection.drop()
    return None


def data_insert_test():
    """
     Inserting Demo Data for Testing
    """
    RecipeService.SelectedRecipes(575469)
    return None


class Service(unittest.TestCase):
    """
    Testing all the Services
    """
    def test_get_ingredients_Service(self):
        response = IngredientService.get_ingredients()
        assert len(response) == 1000

    def test_Recipe_Service(self):
        response = RecipeService.getRecipes('almonds')
        assert len(response) == 20

    def test_SelectedRecipe_Service(self):
        response = RecipeService.SelectedRecipes(575469)
        data_remove_test()
        assert response == "All the Ingredients are added to your shopping List for this recipe"

    def test_ShoppingBag_Service(self):
        data_insert_test()
        response = IngredientService.ShoppingBag()
        data_remove_test()
        assert response == [{'Ingredients': [
            {'_id': 1082047, 'name': 'kosher salt', 'aisle': 'Spices and Seasonings'},
            {'_id': 11529, 'name': 'tomatoes', 'aisle': 'Produce'},
            {'_id': 11529, 'name': 'tomatoes', 'aisle': 'Produce'},
            {'_id': 11529, 'name': 'whole tomatoes', 'aisle': 'Produce'},
            {'_id': None, 'name': 'place the mixture in a colander that has been lined', 'aisle': '?'}],
            'Average price per Recipe': 170.68, 'Recipe Name': 'Clear Tomato Martini'}]


class Repo(unittest.TestCase):
    """
        Testing all the Repos
    """
    def test_ingredient_All_Repo(self):
        res = IngredientRepo.getAll()
        assert len(res) == 1000

    def test_get_Recipe_Repo(self):
        response = RecipeRepo.QueryRecipe('almonds')
        res = json.loads(response.content)
        assert len(res) == 20

    def test_SelectedRecipe_Service(self):
        response = RecipeRepo.selectRecipe(575469)
        res = json.loads(response.content)
        data_remove_test()
        assert res['title'] == 'Clear Tomato Martini'

    def test_selectedIngredients_Repo(self):
        ingredient = {'Recipe Name': 'Clear Tomato Martini',
                      'Ingredients': [
                          {'_id': 1082047,
                           'name': 'kosher salt',
                           'aisle': 'Spices and Seasonings'},
                          {'_id': 11529, 'name': 'tomatoes', 'aisle': 'Produce'},
                          {'_id': 11529, 'name': 'tomatoes', 'aisle': 'Produce'},
                          {'_id': 11529, 'name': 'whole tomatoes', 'aisle': 'Produce'},
                          {'_id': None, 'name': 'place the mixture in a colander that has been lined', 'aisle': '?'}
                      ],
                      'price': 170.68}
        res = IngredientRepo.selectedIngredients(ingredient)
        data_remove_test()
        assert res == "Item Added to your shopping bag"

    def test_ShoppingBag_Repo(self):
        data_insert_test()
        response = IngredientRepo.shoppingBag()
        data_remove_test()
        assert len(response) != 0
