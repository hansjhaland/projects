from django.test import TestCase
from user.models import User
from recipe.models import Recipe

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(fname="first", lname="last")
        User.objects.create(username="olanor", password="olanor123", fname="Ola", lname="Normann", email="ola@normann.no")
        Recipe.objects.create(title="Pizza", ingredients="Ost, Tomatsaus, Bunn", description="Veldig god :)", user_id=2)
        Recipe.objects.create(title="Burger", ingredients="Brød, Kjøtt, Brød", description="Saftig", user_id=2)
        User.objects.create(username="g-man", password="geir123", fname="Geir", lname="Due", email="geir@due.no")

    def test_user_exist(self):
        self.assertTrue(User.objects.filter(fname="first").exists())
        self.assertFalse(User.objects.filter(fname="second").exists())

    def test_user_id(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.fname, "first")
        self.assertEqual(user.lname, "last")

    def test_user_recipe(self):
        self.assertTrue(Recipe.objects.filter(user=2).exists())
        self.assertFalse(Recipe.objects.filter(user=3).exists())

        
        
