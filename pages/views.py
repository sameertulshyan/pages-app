from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
	"""docstring for HomePageView"""
	template_name = 'home.html'

class AboutPageView(TemplateView):
	"""docstring for AboutPageView"""
	template_name = 'about.html'
		