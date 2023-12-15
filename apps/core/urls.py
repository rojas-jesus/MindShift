from django.urls import path
from .views import (
        home, 
        ThoughtListView, 
        ThoughtCreateView, 
        ThoughtDetailView,
        ThoughtUpdateView,
        ThoughtDeleteView,
        ThoughtDateListView,
        ThoughtDateCreateView,
        ThoughtDateDetailView,
        ThoughtDateUpdateView,
        ThoughtDateDeleteView,
        most_relevant_thoughts, 
        ActionListView,
        ActionCreateView, 
        ActionDetailView,
        ActionUpdateView,
        ActionDeleteView,
        action_emotion_chart_view,
        )


app_name = "core"

urlpatterns = [
    path("home/", home, name = "home" ),

    path("thoughts/", ThoughtListView.as_view(), name = "thought-list"),
    path("thought/create/", ThoughtCreateView.as_view(), name = "thought-create"),
    path("thought/<int:pk>/", ThoughtDetailView.as_view(), name = "thought-detail"),
    path("thought/<int:pk>/update/", ThoughtUpdateView.as_view(), name="thought-update"),
    path("thought/<int:pk>/delete/", ThoughtDeleteView.as_view(), name="thought-delete"),

    path("thought-dates/", ThoughtDateListView.as_view(), name = "thought-date-list"),
    path("thought-date/create/", ThoughtDateCreateView.as_view(), name = "thought-date-create"),
    path("thought-date/<int:pk>/", ThoughtDateDetailView.as_view(), name = "thought-date-detail"),
    path("thought-date/<int:pk>/update/", ThoughtDateUpdateView.as_view(), name = "thought-date-update"),
    path("thought-date/<int:pk>/delete/", ThoughtDateDeleteView.as_view(), name = "thought-date-delete"),

    path("most-relevant-thoughts/", most_relevant_thoughts, name = "most-relevant-thoughts"),

    path("actions/", ActionListView.as_view(), name="action-list"),
    path("action/create/", ActionCreateView.as_view(), name="action-create"),
    path("action/<int:pk>/", ActionDetailView.as_view() , name="action-detail"),
    path("action/<pk>/update/", ActionUpdateView.as_view(), name="action-update"),
    path("action/<pk>/delete/", ActionDeleteView.as_view(), name="action-delete"),


    path("action-emotion-chart/", action_emotion_chart_view, name="action-emotion-chart"),

]
