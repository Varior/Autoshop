from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.
class Main(TemplateView):
    template_name = 'index.html'
