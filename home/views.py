from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "home.html"

class SigninView(generic.TemplateView):
    template_name = "login.html"
