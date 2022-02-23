from turtle import title
from django.db import models
from django.forms import ModelForm
from user.models import User

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    publishedDate = models.DateTimeField("date published", auto_now_add=True)
    ingredients = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    public = models.BooleanField(default=False) # if true, the recipe should show up in the public feed
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        exclude = ["user"]
        

        #fields = ["title", "publishedDate", "ingredients", "description"]


