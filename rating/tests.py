from django.test import TestCase
from .models import Entry

# Create your tests here.
class EntryModelTest(TestCase):

    def test_string_representation(self):
        entry = Entry(rating='5')
        self.assertEqual(str(entry), entry.rating)

class WebpageTest(TestCase):

    def test_homepage(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
