from turtle import title
from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    publishedDate = models.DateTimeField("date published")
    ingredients = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title+self.publishDate

