from django.test import TestCase, Client
from django.urls import reverse 


class TestViews(TestCase):
    

    def setUp(self):
        self.client = Client()

        self.signupUrl = reverse('signup')
        self.loginUrl = reverse('login')
        self.usersUrl = reverse('show all the users in the system')
        self.user1 = reverse('user', args = [1]) # Shows the first user in the mockDB

    def test_register(self):

        response = self.client.get(self.signupUrl)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_POST(self):
        pass