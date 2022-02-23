from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate # going to be used later
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from user.models import UserForm
# from user.models import Login
from user.models import LoginForm
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

# def user(response, id):
#     person = User.objects.get(id=id)
#     return render(response, "user/user.html", {"name":(person.fname + ' ' + person.lname)})
def user(response, id):
    person = User.objects.get(id=id)
    recipeList = Recipe.objects.filter(user=id)
    return render(response, "user/user.html", {"person":person, "recipeList":recipeList})

def login(request):
    print("hellooo folkens")
    if( request.method == "post"):
        form = LoginForm(request.POST)
        print(form.is_valid() + "hallo")
        if form.is_valid():
            form_data = form.cleaned_data
            input_username = form_data['username']
            input_password = form_data['password']
            print(input_username, input_password)
            if User.objects.filter(input_username).exists():
                user = User.objects.get(username = input_username)
                if user.password == input_password:
                    return HttpResponseRedirect('/user/%i' % user.id)
            
    # user = User.objects.filter(id = id)
    # if( request.method == "post"):
    #     form = Login(request.POST)
    else:
        form = LoginForm()
        print("Her er det noe feil")
    
    return render(request, "login.html", {"form":form})