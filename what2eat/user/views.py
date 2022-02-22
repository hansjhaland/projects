from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate # going to be used later
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from user.models import UserForm
from recipe.models import Recipe

# Create your views here.

def index(response):
    return HttpResponse("Hello everyone, this is supposed to be the mainpage, this should probably be in a separate 'app', but for now this will have to do.\n This is now inside our 'register-app'")

def signup(request):
    if( request.method == "post"):
        form = UserForm(request.POST)
        if(form.is_valid()):
            #Here we save a new user based on information from the form if valid
            #Here we can navigate to /user maybe 
            pass
    else:
        form = UserForm()
    
    return render(request, "register.html", {"form":form})

def hello(response):
    return HttpResponse("Hello the redirect works!")

def user(response, id):
    person = User.objects.get(id=id)
    recipeList = Recipe.objects.filter(user=id)
    return render(response, "user/user.html", {"person":person, "recipeList":recipeList})


    