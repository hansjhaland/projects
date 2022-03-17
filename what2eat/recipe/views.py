from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe, RecipeForm, categoryForm
from user.models import User

# Create your views here.

def show_all_recipes(request):
    recipeList = Recipe.objects.all()
    print(recipeList)
    context = {'recipeList':recipeList, 'form': categoryForm()}

    if request.method == "POST":
        form = categoryForm(request.POST)

        if form.is_valid():
            
            option = form.cleaned_data
            print (option)
            if (option.get('option') ==  "breakfast"):
                recipeList = Recipe.objects.filter(category="breakfast")
            if (option.get('option') == "lunch" ):
                recipeList = Recipe.objects.filter(category="lunch")
            if (option.get('option') == "dinner"):
                recipeList = Recipe.objects.filter(category="dinner")
            print(recipeList)
            context = {'recipeList': recipeList, "form":categoryForm()}
        return render(request, "feed.html", context)


    # latestRecipeList = Recipe.objects.order_by("-publishedDate")
    # print(latestRecipeList)
    # context = {'latestRecipeList':latestRecipeList}
    return render(request, "recipe.html", context)

    
def create_recipe(request, userID):
    #print("Her er jeg")
    user = User.objects.get(id=userID)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecipeForm(request.POST,  request.FILES)
        #print(form.data["user"])

        # check whether it's valid:
        if form.is_valid():
            print("the form is valid")
            # process the data in form.cleaned_data as required
            title = form.cleaned_data["title"]
            ingredients = form.cleaned_data["ingredients"]
            description = form.cleaned_data["description"]
            category = form.cleaned_data["category"]
            

            form.save()
            # redirect to a new URL, This gets overidden by on action in html if anything is written there
            return HttpResponseRedirect("/"+form.data["user"]+ "/")

    else:
        # if a GET (or any other method) we'll create a blank form
        form = RecipeForm()

    return render(request, 'recipeForm.html', {'form': form, 'user':user})

def show_recipe(request, userID, id):
    recipe = Recipe.objects.get(id=id)
    user = User.objects.get(id=userID)

    if request.method == 'POST':
        recipe.delete()
        return redirect('/%i' % userID)

    return render(request, "recipe/selected.html", {"recipe":recipe, "user":user})

def editRecipe(request, id, userID):
    recipe = Recipe.objects.get(id=id)
    user = User.objects.get(id=userID)
    title = recipe.title
    publishedDate = recipe.publishedDate
    ingredients = recipe.ingredients
    description = recipe.description
    public = recipe.public
    category = recipe.category
    picture = recipe.picture
    print(picture)
    form = RecipeForm({'title': title, 'publishedDate':publishedDate, 'ingredients':ingredients, 'public':public, 'category':category, 'description':description, 'picture':picture, 'user':user})

    if(str(recipe.picture) != "/images/defaultRecipeImage.jpg"):
            recipe.picture.delete(False)

    if (request.method == "POST"):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            # publishedDate will not be updated here (maybe not let anyone change it later)
            newRecipe = Recipe.objects.get(id=id)
            newRecipe.ingredients = form.cleaned_data["ingredients"]
            newRecipe.description = form.cleaned_data["description"]
            newRecipe.title = form.cleaned_data['title']
            newRecipe.public = form.cleaned_data['public']
            newRecipe.category = form.cleaned_data["category"]
            newRecipe.picture = form.cleaned_data["picture"]

            newRecipe.save()

    return render(request, 'recipeForm.html', {'form':form, 'user':user})


def showFeed(request, userID):
    recipeList = Recipe.objects.filter(public=True)
    user = User.objects.get(id=userID)
    #return render(response, "feed.html", context)
    print(recipeList)
    context = {'recipeList':recipeList, 'form': categoryForm(), 'user':user}

    if request.method == "POST":
        form = categoryForm(request.POST)

        if form.is_valid():
            
            option = form.cleaned_data
            print (option)
            if (option.get('option') ==  "all"):
                recipeList = Recipe.objects.filter(public=True)
            if (option.get('option') ==  "breakfast"):
                recipeList = Recipe.objects.filter(category="breakfast", public=True)
            if (option.get('option') == "lunch" ):
                recipeList = Recipe.objects.filter(category="lunch", public=True)
            if (option.get('option') == "dinner"):
                recipeList = Recipe.objects.filter(category="dinner", public=True)
            print(recipeList)
            context = {'recipeList': recipeList, "form":categoryForm(), 'user':user}
        return render(request, "feed.html", context)


    # latestRecipeList = Recipe.objects.order_by("-publishedDate")
    # print(latestRecipeList)
    # context = {'latestRecipeList':latestRecipeList}
    return render(request, "feed.html", context)
