from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def user(response):
    form = UserCreationForm()
    return render(response, "user.html", {"form":form})