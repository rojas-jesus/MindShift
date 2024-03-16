from django.urls import path
from .views import home, about_us


app_name = "homepage"

urlpatterns = [
    path("home/", home, name = "home" ),
    path("about-us/", about_us, name = "about-us" ),
    ]
