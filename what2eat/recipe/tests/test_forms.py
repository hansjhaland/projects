from django.test import TestCase
from recipe.models import categoryForm, RecipeForm
from user.models import User


class TestForms(TestCase):
    
    def test_recipe_form(self):
        user = User.objects.create(username="olanor", password="olanor123", fname="Ola", lname="Normann", email="ola@normann.no")

        form = RecipeForm(data = {})
        self.assertEquals(len(form.errors), 5)
        improvedForm = RecipeForm(data = {'title':'Spaghetti', 'ingredients':'pasta', 'description':'cook the pasta!!!', 'user':user, 'email':'hei123@noe.no', 'category':'breakfast' })
        self.assertTrue(improvedForm.is_valid())


    def test_category_form(self):
        form = categoryForm()
        self.assertFalse(form.is_valid())
        improvedform = categoryForm(data = {'option':'breakfast'})
        self.assertTrue(improvedform.is_valid())