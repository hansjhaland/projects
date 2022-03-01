from django.urls import path 
from . import views 

# here you define the paths to our webpages (from this register-app)


urlpatterns = [
    # path("recipe/filter", views.show_selected_recipes, name="recipeFilter") #This function will be used when the filterbutton is clicked.
    # path("", views.index, name = "index"), # if you now go to the home directory, it will go to views.index, and it shows the function named index
    path("recipe/", views.show_all_recipes, name ="show_all_recipes"), #list of all recipes in db, for developers
    path("<int:userID>/recipe/form/", views.create_recipe, name ="create_recipe"), 
    path("<int:userID>/recipe/<int:id>/", views.show_recipe, name ="show_recipe"), #list of public recipes
    path("<int:userID>/recipe/<int:id>/edit/", views.editRecipe, name="editRecipe"),
    path("<int:userID>/feed/", views.showFeed, name="showFeed")
]
