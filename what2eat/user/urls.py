from django.urls import path 
from . import views 

# here you define the paths to our webpages (from this register-app)


urlpatterns = [
    path("user/", views.user, name ="user")
]
