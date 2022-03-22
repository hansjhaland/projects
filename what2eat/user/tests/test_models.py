from django.test import TestCase
from user.models import User

class TestModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username="olanor", password="olanor123",
            fname="Ola", lname="Normann", 
            email="ola@normann.no")

        
    def test_user_exist(self):
        self.assertTrue(User.objects.filter(fname="Ola").exists())
        self.assertFalse(User.objects.filter(fname="second").exists())

    def test_user_id(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.fname, "Ola")
        self.assertEqual(user.lname, "Normann")

   
        
        