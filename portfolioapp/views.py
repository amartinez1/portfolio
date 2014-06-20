from django.shortcuts import render
from django.views.generic import TemplateView

class Indexview(TemplateView):
	template_name = 'index.html'
	


# Create your views here.
