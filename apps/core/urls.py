from django.urls import path
from .views import Home, ThoughtsList

urlpatterns = [
    path("home/", Home, name = "Home" ),
    path("thoughtslist/", ThoughtsList, name = "ThoughtsList"),
]
