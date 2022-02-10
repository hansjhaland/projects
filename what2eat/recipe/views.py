from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Recipe, RecipeForm

# Create your views here.
def index(response):
    return HttpResponse("frrrr")

def recipeshow(response):
    latestRecipeList = Recipe.objects.order_by("-publishedDate")
    print(latestRecipeList)
    context = {'latestRecipeList':latestRecipeList}
    return render(response, "recipe.html", context)
    
def create_recipe(request):
    print("Her er jeg")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecipeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("the form is valid")
            # process the data in form.cleaned_data as required
            # title = form.cleaned_data["title"]
            # publishedDate = form.cleaned_data["publishedDate"]
            # ingredients = form.cleaned_data["ingredients"]
            # description = form.cleaned_data["description"]
            form.save()
            # redirect to a new URL, This gets overidden by on action in html??
            return HttpResponseRedirect('/recipe/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecipeForm()

    return render(request, 'recipeForm.html', {'form': form})