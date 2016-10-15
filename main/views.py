from django.shortcuts import render
from . import templates

# Create your views here.

def home_page(request):
	return render(request, "home.html")

def create_account(request):
	return render(request, "create_account.html")
