from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'eleven/home.html'

class AboutView(TemplateView):
	template_name = 'eleven/about.html'
