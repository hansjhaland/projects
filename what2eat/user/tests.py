from django.test import TestCase
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(fname="first", lname="last")

    def test_user_exist(self):
        self.assertTrue(User.objects.filter(fname="first").exists())
        self.assertFalse(User.objects.filter(fname="second").exists())

    def test_user_id(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.fname, "first")
        self.assertEqual(user.lname, "last")

        
        
