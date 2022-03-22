from django.test import SimpleTestCase
from django.urls import reverse, resolve
from recipe.views import show_all_recipes, create_recipe, show_recipe, editRecipe, showFeed

class TestUrls(SimpleTestCase):

    def test_all_recipes(self):
        url = reverse('show_all_recipes')
        self.assertEquals(resolve(url).func, show_all_recipes)

    def test_create_recipe_user1(self):
        url = reverse('create_recipe', args = [1])
        self.assertEquals(resolve(url).func, create_recipe)

    def test_show_recipe(self):
        url = reverse('show_recipe', args = [1, 1])
        self.assertEquals(resolve(url).func, show_recipe)

    def test_edit_recipe(self):
        url = reverse('editRecipe', args = [1, 1])
        self.assertEquals(resolve(url).func, editRecipe)
    
    def test_feed(self):
        url = reverse('showFeed', args=[1])
        self.assertEquals(resolve(url).func, showFeed)