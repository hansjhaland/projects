from django.urls import path 
from . import views 
# here you define the paths to our webpages (from this user-app)


urlpatterns = [
    # path("", views.index, name="index")
    path("hello/", views.hello, name="hello"),
    path("user/", views.listAllUsers, name= "show all the users in the system"),
    path("<int:id>/", views.user, name ="user"),
    path("register/", views.signup, name = "signup")
]
