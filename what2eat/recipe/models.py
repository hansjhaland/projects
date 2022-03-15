from asyncio.windows_events import NULL
from tkinter import HIDDEN, Widget
from turtle import title
from unicodedata import category
from django.db import models
from django import forms
from django.forms import ModelForm
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

CHOICES = [("breakfast", "Frokost"),("lunch", "Lunsj"), ("dinner", "Middag")]
RATING = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    publishedDate = models.DateTimeField("date published", auto_now_add=True)
    ingredients = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    public = models.BooleanField(default=False) # if true, the recipe should show up in the public feed
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=10,choices = CHOICES)

    def __str__(self):
        return self.title + self.category

class Rating(models.Model):
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    

    class Meta:
        unique_together = (("user", "recipe"),)
        
        
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        #exclude = ["user"]
        widgets = {
             "user": forms.HiddenInput()
        }
        #fields = ["title", "publishedDate", "ingredients", "description"]

class categoryForm(forms.Form):
    CHOICES.insert(0,("all", "Alle"))
    option = forms.ChoiceField(choices=CHOICES, label="", widget=forms.RadioSelect)

class RatingForm(forms.Form):
    option = forms.ChoiceField(choices=RATING, label="", widget=forms.RadioSelect)



