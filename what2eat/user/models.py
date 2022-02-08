from pickle import TRUE
from django.db import models

# Create your models here.
class User(models.Model): 
    fname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    
    def __str__(self):
        return self.fname + " " + self.surname