from pickle import TRUE
from django.db import models
from django.forms import ModelForm
from django import forms

#Man bruker modeller for å dra informasjon fra database og inn i "appen"

# Create your models here.

class User(models.Model):
    username = models.CharField('Brukernavn', max_length=200)
    password = models.CharField('Passord', max_length=200)
    fname = models.CharField('Fornavn', max_length=200)
    lname = models.CharField('Etternavn',max_length=200)
    email = models.CharField('E-post', max_length=200)

    def __str__(self):
        return self.fname + " " + self.lname


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput() 
        }

"""
class User(models.Model):

    # ID is created by Django when you add to DB, not sure how to get it in here yet


    def __init__(self, fname, surname, email, password, dateOfBirth, recipes, ratedRecipes):

        if (fname == None or surname == None or email == None or dateOfBirth == None or password == None):
            raise Error("Firstname, surname, date of birth, password and email cannot be null!")   # Can create problems if a user can delete either of these
            
        self.fname = fname
        self.surname = surname
        self.email = email
        self.dateOfBirth = dateOfBirth
        self.password = password
        if(recipes == None):
            recipes = []
        else:     
            self.recipes = recipes
        if(ratedRecipes == None):
            ratedRecipes = {}
        else:     
            self.ratedRecipes = ratedRecipes
        
        

    def __str__(self):
        return "Hi my name is" + self.fname + self.surname + ", and my email is: " + self.email

    def addRecipe(self, recipe):
        if recipe not in self.recipes: 
            self.recipes.append(recipe)
        else:
            raise Error("Recipe already your list of recipes!")
        return # not sure if needed

    def removeRecipe(self, recipe):
        if(recipe not in self.recipes):
            raise Error("You dont have this recipe in your list!")
        else: 
            self.recipes.pop(recipe)

    def rateRecipe(self, recipe, stars):
        self.ratedRecipes[recipe] = stars

    def removeRatedRecipe(self, recipe):
        return

    def saveToDb(self):
        # Find a way to save this to our db as a JSONobject i think, possibly with the attributes as keys
        return

"""

