from django.db import models

class Entry(models.Model):
    rating = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
