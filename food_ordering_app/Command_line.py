from food_ordering_app.service import IngredientService
from food_ordering_app.service import RecipeService
from food_ordering_app.model import Exception


def command_line():
    """
    This function for Command line execution of the application
    """
    response = IngredientService.get_ingredients()
    print(response)
    query = input("Please enter the Ingredients")
    while True:
        try:
            response = RecipeService.getRecipes(query)
            for item in response:
                print(item)
                user_response = input("Do you like this recipe")
                if user_response == "Y" or user_response == "y":
                    choice = item['id']
                    response = RecipeService.SelectedRecipes(choice)
                    print(response)
                    response = IngredientService.ShoppingBag()
                    return "This is the Shopping Bag", response
                else:
                    continue
        except ValueError:
            raise ValueError(Exception.Ingredient_404, 404)
        query = input("Please re-enter the Ingredient from the Ingredients list")


print(command_line())
