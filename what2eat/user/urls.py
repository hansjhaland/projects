from django.urls import path 
from . import views 

# here you define the paths to our webpages (from this user-app)


urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("user/", views.user, name ="user"),
    path("register/", views.signup, name = "signup"),
    path("", views.index, name="index")
]
