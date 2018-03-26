from django.db import models
from django import forms

class Entry(models.Model):
    rating = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.rating
        
