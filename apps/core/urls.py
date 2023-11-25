from django.urls import path
from .views import Home, ThoughtsList, CreateThought, CreateThoughtDate, MostRelevantThoughts, ActionCreateView, ActionUpdateView


urlpatterns = [
    path("home/", Home, name = "Home" ),
    path("thoughtslist/", ThoughtsList, name = "ThoughtsList"),
    path("createthought/", CreateThought.as_view(), name = "CreateThought"),
    path("createthoughtdate/", CreateThoughtDate.as_view(), name = "CreateThoughtDate"),
    path("mostrelevantthoughts/", MostRelevantThoughts, name = "MostRelevantThoughts"),

    path("action/create/", ActionCreateView.as_view(), name="action_create"),
    path("action/<pk>/update/", ActionUpdateView.as_view(), name="action_update"),

]
