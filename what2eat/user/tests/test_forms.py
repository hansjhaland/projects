from django.test import SimpleTestCase
from user.models import LoginForm, UserForm

class TestForms(SimpleTestCase):

    def test_login_form(self):
            form = LoginForm(data={'username':'Ola122', 'password':'123hei'})

            self.assertTrue(form.is_valid())


    def test_user_form(self):
        falseform = UserForm(data = {})
        self.assertEquals(len(falseform.errors), 5)
        form = UserForm ( data = {'username':'Olahal', 'password':'halvorsen123', 'fname':'Ola', 'lname':'Halvorsen', 'email':'ola@halvorsen.no'})

        self.assertTrue(form.is_valid())