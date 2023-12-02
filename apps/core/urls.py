from django.urls import path
from .views import Home, ThoughtsList, ThoughtCreateView, ThoughtDateCreateView, MostRelevantThoughts, ActionCreateView, ActionUpdateView, ActionDetailView


urlpatterns = [
    path("home/", Home, name = "Home" ),
    path("thoughtslist/", ThoughtsList, name = "ThoughtsList"),
    path("thought/create/", ThoughtCreateView.as_view(), name = "thought-create"),
    path("thought-date/create/", ThoughtDateCreateView.as_view(), name = "thought-date-create"),
    path("mostrelevantthoughts/", MostRelevantThoughts, name = "MostRelevantThoughts"),

    path("action/create/", ActionCreateView.as_view(), name="action_create"),
    path("action/<pk>/update/", ActionUpdateView.as_view(), name="action_update"),
    path("action/<int:pk>/", ActionDetailView.as_view() , name="action_detail"),

]
