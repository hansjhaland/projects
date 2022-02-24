from datetime import datetime
from unicodedata import category
from django.test import TestCase
from .models import Recipe
from user.models import User

# Create your tests here.
class RecipeTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="olanor", password="olanor123", fname="Ola", lname="Normann", email="ola@normann.no")
        Recipe.objects.create(title="Pizza", ingredients="Cheese, Meat", description="This is very good :)", user_id=1, category="Dinner")

    def test_recipe_exist(self):
        self.assertTrue(Recipe.objects.filter(title="Pizza").exists())
        self.assertFalse(Recipe.objects.filter(title="Burger").exists())

    def test_recipe_id(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.title, "Pizza")
        self.assertEqual(recipe.ingredients, "Cheese, Meat")
        self.assertEqual(recipe.description, "This is very good :)")
        self.assertEqual(recipe.category, "Dinner")
        #self.assertEqual(recipe.publishedDate, datetime.now())