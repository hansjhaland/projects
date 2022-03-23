from email import message
from distutils.dep_util import newer_pairwise
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import RatingForm, Recipe, RecipeForm, categoryForm, Rating
from user.models import User
from django.db.models import Avg
from django.contrib import messages

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
    colorMode = user.darkmode
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
            messages.error(request, ("Oppskrift opprettet"))

            return HttpResponseRedirect("/"+form.data["user"]+ "/")
        else:
            messages.error(request, "Det gikk ikke å lage en oppskrift")

    else:
        # if a GET (or any other method) we'll create a blank form
        form = RecipeForm()

    return render(request, 'recipeForm.html', {'form': form, 'user':user, "colorMode":colorMode})


def show_recipe(request, userID, id):
    recipe = Recipe.objects.get(id=id)
    user = User.objects.get(id=userID)
    form = RatingForm()
    #rating_entry = Rating.objects.filter(user_id = userID, recipe_id = id)
    if Rating.objects.filter(user_id = userID, recipe_id = id).exists():
        rating_entry = Rating.objects.filter(user_id = userID, recipe_id = id)
        form = RatingForm({'rating': rating_entry[:1].get().rating, 'rating_form': True, 'user': userID, 'recipe': id})
    
    colorMode = user.darkmode
    context = {'recipe':recipe, 'form': form, 'user':user, "colorMode":colorMode}
    

    if request.method == 'POST':
        if "rating_form" in request.POST:
            form = RatingForm(request.POST)
            if form.is_valid():
                if Rating.objects.filter(user_id = userID, recipe_id = id).exists():
                    rating = Rating.objects.get(user_id=userID, recipe_id=id)
                    rating.rating = form.cleaned_data["rating"]
                    rating.save()
                else:
                    form.save()
            else:
                print(form.errors.as_data())
            new_avg_rating = Rating.objects.filter(recipe_id = id).aggregate(Avg('rating'))
            Recipe.objects.filter(id = id).update(avg_rating = new_avg_rating['rating__avg'])
                
            context = {'recipe':recipe, 'form': form, 'user':user}

            return HttpResponseRedirect("#")
        else:    
            recipe.delete()
            messages.success(request, "Du har slettet oppskriften")
            return redirect('/%i' % userID)

    return render(request, "recipe/selected.html", context)


def editRecipe(request, id, userID):
    recipe = Recipe.objects.get(id=id)
    user = User.objects.get(id=userID)
    title = recipe.title
    publishedDate = recipe.publishedDate
    ingredients = recipe.ingredients
    method = recipe.method
    description = recipe.description
    public = recipe.public
    category = recipe.category
    rating = recipe.avg_rating
    print(f"RATING FØR:{rating}")
    picture = recipe.picture
    cooking_time = recipe.cooking_time
    print(picture)
    form = RecipeForm({'title': title, 'publishedDate':publishedDate, 'ingredients':ingredients, 'public':public, 'category':category, 'description':description, 'picture':picture, 'user':user, 'avg_rating': rating, 'cooking_time': cooking_time, 'method':method})

    if(str(recipe.picture) != "/images/defaultRecipeImage.jpg"):
            recipe.picture.delete(False)

    colorMode = user.darkmode
    
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
            newRecipe.avg_rating = form.cleaned_data["avg_rating"]
            newRecipe.cooking_time = form.cleaned_data["cooking_time"]
            newRecipe.method = form.cleaned_data["method"]

            newRecipe.save()
            messages.error(request, ("Du har endret oppskriften"))

            print(f"RATING ETTER:{rating}")

    return render(request, 'recipeForm.html', {'form':form, 'user':user, "colorMode":colorMode})


def showFeed(request, userID):
    recipeList = Recipe.objects.filter(public=True)
    user = User.objects.get(id=userID)
    #return render(response, "feed.html", context)
    print(recipeList)
    
    colorMode = user.darkmode
    context = {'recipeList':recipeList, 'form': categoryForm(), 'user':user, "colorMode":colorMode}

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
