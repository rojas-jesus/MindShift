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
        most_relevant_thoughts_view, 
        ActionListView,
        ActionCreateView, 
        ActionDetailView,
        ActionUpdateView,
        ActionDeleteView,
        #action_emotion_chart_view,
        #actiondate_sad_intensity_chart_view,
        #actiondate_today_sad_intensity_chart_view,
        # Charts
        actiondate_sad_intensity_last_30_days_view,
        ChartsView,
        FacilitatorCreateView,
        FacilitatorRetrieveView,
        EnvironmentCreateView,
        EnvironmentRetrieveView,
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

    path("most-relevant-thoughts/", most_relevant_thoughts_view, name = "most-relevant-thoughts"),

    path("actions/", ActionListView.as_view(), name="action-list"),
    path("action/create/", ActionCreateView.as_view(), name="action-create"),
    path("action/<int:pk>/", ActionDetailView.as_view() , name="action-detail"),
    path("action/<pk>/update/", ActionUpdateView.as_view(), name="action-update"),
    path("action/<pk>/delete/", ActionDeleteView.as_view(), name="action-delete"),


    #path("action-emotion-chart/", action_emotion_chart_view, name="action-emotion-chart"),
    #path("action-date-sad-intensity-chart/", actiondate_sad_intensity_chart_view, name="action-date-sad-intensity-chart"),
    #path("action-date-today-sad-intensity-chart/", actiondate_today_sad_intensity_chart_view, name="action-date-today-sad-intensity-chart"),
    path("action-date/chart/sad-intensity-last-30-days/", actiondate_sad_intensity_last_30_days_view, name="action-date-chart-sad-intensity-last-30-days"),
    path("charts/", ChartsView.as_view(), name="charts"),

    # Api

    path("facilitator/create/", FacilitatorCreateView.as_view(), name="facilitator-create"),
    path("facilitator/<id>/", FacilitatorRetrieveView.as_view(), name="facilitator-retrieve"),

    path("environment/create/", EnvironmentCreateView.as_view(), name="environment-create"),
    path("environment/<id>/", EnvironmentRetrieveView.as_view(), name="environment-retrieve"),
]
