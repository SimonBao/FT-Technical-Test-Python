from django.db import models

class WebpageTest(self):
    res = self.client.get('/')
    self.assertEqual(res.status_code, 200)

class Entry(models.Model):
    rating = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.rating
