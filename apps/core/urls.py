from django.urls import path
from .views import Home, ThoughtsList, CreateThought


urlpatterns = [
    path("home/", Home, name = "Home" ),
    path("thoughtslist/", ThoughtsList, name = "ThoughtsList"),
    path("createthought/", CreateThought.as_view(), name = "CreateThought"),
]
