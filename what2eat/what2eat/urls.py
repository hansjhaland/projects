"""what2eat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recipe import views as recv
from user import views as userv


urlpatterns = [
    path('', userv.index, name="index"),
    path('admin/', admin.site.urls),
    path('', include("recipe.urls")),
    path('register/', userv.signup, name="signup"),
    path('user/', userv.user, name="user"),
    path('recipe/', recv.recipeshow, name = "recipeshow" ),
    path("recipe/form/", recv.create_recipe, name ="create_recipe"),
    path('hello/', userv.hello, name = "hello"),
    path('user/<int:id>', userv.user, name="user")
]