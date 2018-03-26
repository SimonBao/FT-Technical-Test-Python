from django.shortcuts import render
from django.views.generic.base import TemplateView
# Imports templates defined in settings.py

class HomeView(TemplateView):
    template_name = 'index.html'
    
