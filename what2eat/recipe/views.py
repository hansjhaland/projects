from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe

# Create your views here.
def index(response):
    return HttpResponse("frrrr")

def recipeshow(response):
    latestRecipeList = Recipe.objects.order_by("-publishedDate")
    print(latestRecipeList)
    context = {'latestRecipeList':latestRecipeList}
    return render(response, "recipe.html", context)
    
