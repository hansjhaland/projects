from datetime import datetime
from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(title="Pizza", ingredients="Cheese, Meat", description="This is very good :)")

    def test_recipe_exist(self):
        self.assertTrue(Recipe.objects.filter(title="Pizza").exists())
        self.assertFalse(Recipe.objects.filter(title="Burger").exists())

    def test_recipe_id(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.title, "Pizza")
        self.assertEqual(recipe.ingredients, "Cheese, Meat")
        self.assertEqual(recipe.description, "This is very good :)")
        #self.assertEqual(recipe.publishedDate, datetime.now())