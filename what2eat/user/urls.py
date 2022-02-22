from django.urls import path 
from . import views 
# here you define the paths to our webpages (from this user-app)


urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("user/"+"<int:id>", views.user, name ="user"),
    path("register/", views.signup, name = "signup"),
    path("login/", views.login, name = "login"),
    path("", views.index, name="index")
]
