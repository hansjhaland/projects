from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import login, register, listAllUsers, user

class TestUrls(SimpleTestCase):


    def test_funksjonsnavn(self): 
        self.assertEquals(1, 1)

    def test_urlforLoginPage(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_urlforSignupPage(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, register)

    def test_urlforUsersPage(self):
        url = reverse('show all the users in the system')
        self.assertEquals(resolve(url).func, listAllUsers)

    def test_urlforUserPage(self): # Adding argument because the url spesific needs it to go into the user
        url = reverse('user', args = [1])
        self.assertEquals(resolve(url).func, user)
