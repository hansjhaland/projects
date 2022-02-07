from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate # going to be used later
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(response):
    return HttpResponse("Hello everyone, this is supposed to be the mainpage, this should probably be in a separate 'app', but for now this will have to do.\n This is now inside our 'register-app'")

def signup(response):
    form = UserCreationForm()
    return render(response, "register.html", {"form":form})

