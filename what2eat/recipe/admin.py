from django.contrib import admin
from .models import Rating, Recipe

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Rating)