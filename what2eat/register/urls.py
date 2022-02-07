from django.urls import path 
from . import views 

# here you define the paths to our webpages (from this register-app)


urlpatterns = [

    path("", views.index, name = "index"), # if you now go to the home directory, it will go to views.index, and it shows the function named index
    path("register/", views.signup, name ="signup")
]
