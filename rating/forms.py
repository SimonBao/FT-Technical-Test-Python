from django import forms

class EntryForm(forms.Form):
    rating = forms.CharField(max_length=1)
