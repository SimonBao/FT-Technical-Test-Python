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

    def test_review_one(self):
        Entry.objects.create(rating='5')
        res = self.client.get('/')
        self.assertContains(res, '5')

    def test_review_two(self):
        Entry.objects.create(rating='2')
        res = self.client.get('/')
        self.assertContains(res, '2')
