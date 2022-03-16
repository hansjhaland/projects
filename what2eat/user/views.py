from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate # going to be used later
from django.contrib.auth.forms import UserCreationForm
from user.models import User, ColorMode
from user.models import UserForm
# from user.models import Login
from user.models import LoginForm
from recipe.models import Recipe
from django.core.exceptions import ValidationError

from what2eat.user.models import ColorModeForm

# Create your views here.

def register(request):
    if( request.method == "POST"):
        form = UserForm(request.POST)
        if(form.is_valid()):
             #Here we save a new user based on information from the form if valid
            #Here we can navigate to /user maybe 
            form_data = form.cleaned_data
            input_username = form_data['username']
            if User.objects.filter(username = input_username).exists() == False:
                form.save()               
                return HttpResponseRedirect('/')
            else:
                raise form.ValidationError(
                    ('Username exists'),
                    code = 'invalid',
                )
    else:
        form = UserForm()
    
    return render(request, "register.html", {"form":form})

# def user(response, id):
#     person = User.objects.get(id=id)
#     return render(response, "user/user.html", {"name":(person.fname + ' ' + person.lname)})
def user(request, id):
    user = User.objects.get(id=id)
    recipeList = Recipe.objects.filter(user=id)

    colorMode = ColorMode.objects.get(id=1)
    activeValue = colorMode.getActive()
    changeColor(request)
    return render(request, "user/user.html", {"user":user, "recipeList":recipeList, "colorMode":activeValue })

def changeColor(request):
    if( request.method == "POST"):
        form = ColorModeForm(request.POST)
        if form.is_valid():
            colorMode = ColorMode.objects.get(id=1)
            form.save()

def login(request):
    print("hellooo folkens")
    if( request.method == "POST"):
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            input_username = form_data['username']
            input_password = form_data['password']
            if User.objects.filter(username = input_username).exists():
                user = User.objects.get(username = input_username)
                if user.password == input_password:
                    return HttpResponseRedirect('/%i' % user.id)
            
    # user = User.objects.filter(id = id)
    # if( request.method == "post"):
    #     form = Login(request.POST)
    else:
        form = LoginForm()
        # print("Her er det noe feil")
    
    return render(request, "login.html", {"form":form})

def listAllUsers(response):
    userList = User.objects.all()
    return render(response, "listOverUsers.html", {"userList":userList})




    
