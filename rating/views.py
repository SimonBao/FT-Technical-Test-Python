from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import EntryForm

# Imports templates defined in settings.py

class HomeView(TemplateView):
    template_name = 'index.html'

def get_rating(request):
    rating = Entry()
    rating.rating = request.POST.get('rating', '')
    rating.save()
    return HttpResponseRedirect('/')
