from django.shortcuts import render

from django.views.generic.base import TemplateView
#from django.views.generic import (ListView, DetailView)
#from pets.models import Pet

# Create your views here.

class ViewIndex(TemplateView):
    template_name = 'index.html'

