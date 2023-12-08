from django.urls import path
from .views import home


app_name = "homepage"

urlpatterns = [
    path("home/", home, name = "home" ),
    ]
