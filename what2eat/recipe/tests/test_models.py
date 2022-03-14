from unicodedata import category
from django.test import TestCase
from recipe.models import Recipe
from user.models import User
class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="olanor", password="olanor123", fname="Ola", lname="Normann", email="ola@normann.no")

        self.recipe1 = Recipe.objects.create(title="Pizza", ingredients="Ost, Tomatsaus, Bunn", description="This is very good :)", user_id=1, category="Dinner")
        self.recipe2 = Recipe.objects.create(title="Burger", ingredients="Brød, Kjøtt, Brød", description="Saftig", user_id=1)
        

    def test_recipe_exist(self):
        self.assertTrue(Recipe.objects.filter(title="Pizza").exists())
        self.assertTrue(Recipe.objects.filter(title="Burger").exists())
        self.assertFalse(Recipe.objects.filter(title="Spaghetti").exists())

        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.title, "Pizza")
        self.assertEqual(recipe.ingredients, "Ost, Tomatsaus, Bunn")
        self.assertEqual(recipe.description, "This is very good :)")
        self.assertEqual(recipe.category, "Dinner")
