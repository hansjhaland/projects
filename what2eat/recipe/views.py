from multiprocessing import context
from unicodedata import category
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe, RecipeForm

# Create your views here.
def index(response):
    return HttpResponse("frrrr")

def show_all_recipes(response):
    recipeList = Recipe.objects.all()
    print(recipeList)
    context = {'recipeList':recipeList}
    # latestRecipeList = Recipe.objects.order_by("-publishedDate")
    # print(latestRecipeList)
    # context = {'latestRecipeList':latestRecipeList}
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
            title = form.cleaned_data["title"]
            ingredients = form.cleaned_data["ingredients"]
            description = form.cleaned_data["description"]
            category = form.cleaned_data["category"]
            

            form.save()
            # redirect to a new URL, This gets overidden by on action in html??
            return HttpResponseRedirect('/recipe/')

    else:
        # if a GET (or any other method) we'll create a blank form
        form = RecipeForm()

    return render(request, 'recipeForm.html', {'form': form})

def show_recipe(response, id):
    recipe = Recipe.objects.get(id=id)

    if response.method == 'POST':
        recipe.delete()
        return redirect('/recipe')

    return render(response, "recipe/selected.html", {"recipe":recipe})

def editRecipe(request, id):
    recipe = Recipe.objects.get(id=id)
    title = recipe.title
    publishedDate = recipe.publishedDate
    ingredients = recipe.ingredients
    description = recipe.description
    form = RecipeForm({'title': title, 'publishedDate':publishedDate, 'ingredients':ingredients, 'description':description})

    
    if (request.method == "POST"):
        form = RecipeForm(request.POST)
        if form.is_valid():
            # publishedDate will not be updated here (maybe not let anyone change it later)
            recipe = Recipe.objects.get(id=id)
            recipe.ingredients = form.cleaned_data["ingredients"]
            recipe.description = form.cleaned_data["description"]
            recipe.title = form.cleaned_data['title']
            recipe.save()
            print(recipe.description)

        

    return render(request, 'recipeForm.html', {'form':form})

