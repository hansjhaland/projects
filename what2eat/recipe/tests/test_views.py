from django.test import TestCase, Client

class TestViews(TestCase):

    def setUp(self):

        self.client = Client()