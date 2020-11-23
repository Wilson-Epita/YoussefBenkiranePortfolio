from django.test import TestCase
from django.test import Client

class PhotoTest(TestCase):

    def setUp(self):
        c = Client()
        self.response = c.get('/photography')

    def test_server_response(self):
        self.assertEqual(self.response.status_code, 200)

# Create your tests here.
