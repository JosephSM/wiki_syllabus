from django.shortcuts import render
from . import templates

# Create your views here.

def home_page(request):
	return render(request, "home.html")
