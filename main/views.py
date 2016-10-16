from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

from .forms import Create_account_form

def home_page(request):
	return render(request, "home.html")

def loginView(request):
     return render(request, 'login.html')

def create_account(request):
	return render(request, 'create_account.html')


def regact(request):
	form = Create_account_form()
	return render(request, 'create_account.html', {'form':form})



def register_account(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = str(email).split('@')[0]
    password = request.POST.get('password')

    if first_name != "" and last_name != "" and email != "" and password != "":
        if User.objects.filter(username=username).exists():
            return render(request, 'create_account.html', {
                'error_message': "Sadly, this username is taken :(",
            })
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)
        messages.add_message(request, messages.INFO, 'You have successfully registered. Welcome to Student Soup!')
        return redirect(reverse('home'))
    else:
        return render(request, 'create_account.html', {
            'error_message': "All fields must be filled in.",
        })

def login_user(request):
    email = request.POST.get('email')
    username = str(email).split('@')[0]
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(reverse('profile'))
        else:
            return render(request, 'login.html', {
                'error_message': "Oh no, your Student Soup account is disabled.",
            })
    else:
        return render(request, 'login.html', {
            'error_message': "Username or password is incorrect.",
        })

@login_required
def logoutUser(request):
    logout(request)
    return redirect(reverse('home'))

@login_required
def profile(request):
    return render(request, 'profile.html')