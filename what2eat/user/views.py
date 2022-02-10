from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate # going to be used later
from django.contrib.auth.forms import UserCreationForm
from user.models import User

# Create your views here.

def user(response):
    form = UserCreationForm()
    return render(response, "user.html", {"form":form})

# Create your views here.

def index(response):
    return HttpResponse("Hello everyone, this is supposed to be the mainpage, this should probably be in a separate 'app', but for now this will have to do.\n This is now inside our 'register-app'")

def signup(response):
    if( response.method == "POST"):
        form = UserCreationForm(response.POST)
        if(form.is_valid()):
            #Here we save a new user based on information from the form if valid
            newUser = User(form['fname'].value(),form['surname'].value(),form['email'].value(),form['password'].value(),form['dob'].value(),None, None)
            newUser.saveToDb()
            #Here we can navigate to /user maybe 
            redirect("../user/")
    
    else:        
        form = UserCreationForm()
    return render(response, "register.html", {"form":form})

def hello(response):
    return HttpResponse("Hello the redirect works!")