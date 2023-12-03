from django.urls import path
from .views import home, ThoughtListView, ThoughtCreateView, ThoughtDateCreateView, most_relevant_thoughts, ActionCreateView, ActionUpdateView, ActionDetailView


app_name = "core"

urlpatterns = [
    path("home/", home, name = "home" ),
    path("thoughts/", ThoughtListView.as_view(), name = "thought-list"),
    path("thought/create/", ThoughtCreateView.as_view(), name = "thought-create"),
    path("thought-date/create/", ThoughtDateCreateView.as_view(), name = "thought-date-create"),
    path("most-relevant-thoughts/", most_relevant_thoughts, name = "most-relevant-thoughts"),

    path("action/create/", ActionCreateView.as_view(), name="action-create"),
    path("action/<pk>/update/", ActionUpdateView.as_view(), name="action-update"),
    path("action/<int:pk>/", ActionDetailView.as_view() , name="action-detail"),

]
