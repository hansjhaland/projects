from django.urls import path 
from . import views 
# here you define the paths to our webpages (from this user-app)


urlpatterns = [
    path("register/", views.register, name = "signup"),
    path("", views.login, name = "login"),
    path("user/", views.listAllUsers, name= "show all the users in the system"),
    path("<int:id>/", views.user, name ="user"),
]
