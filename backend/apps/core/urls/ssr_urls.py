from django.urls import path
from ..views import (
        # SSR
        ssr_home, 
        SSRThoughtListView,
        SSRThoughtCreateView,
        SSRThoughtDetailView,
        SSRThoughtUpdateView,
        SSRThoughtDeleteView,
        SSRThoughtDateListView,
        SSRThoughtDateCreateView,
        SSRThoughtDateDetailView,
        SSRThoughtDateUpdateView,
        SSRThoughtDateDeleteView,
        SSRActionListView,
        SSRActionCreateView,
        SSRActionDetailView,
        SSRActionUpdateView,
        SSRActionDeleteView,

        # SSR Charts
        ssr_most_relevant_thoughts_view, 
        ssr_action_emotion_chart_view,
        SSRChartsView,
        ssr_actiondate_sad_intensity_today_chart_view,
        ssr_actiondate_sad_intensity_last_30_days_view,

        )

urlpatterns = [

    # SSR
    path("home/", ssr_home, name = "ssr-home" ),

    path("thoughts/", SSRThoughtListView.as_view(), name = "ssr-thought-list"),
    path("thought/create/", SSRThoughtCreateView.as_view(), name = "ssr-thought-create"),
    path("thought/<int:pk>/", SSRThoughtDetailView.as_view(), name = "ssr-thought-detail"),
    path("thought/<int:pk>/update/", SSRThoughtUpdateView.as_view(), name="ssr-thought-update"),
    path("thought/<int:pk>/delete/", SSRThoughtDeleteView.as_view(), name="ssr-thought-delete"),

    path("thought-dates/", SSRThoughtDateListView.as_view(), name = "ssr-thought-date-list"),
    path("thought-date/create/", SSRThoughtDateCreateView.as_view(), name = "ssr-thought-date-create"),
    path("thought-date/<int:pk>/", SSRThoughtDateDetailView.as_view(), name = "ssr-thought-date-detail"),
    path("thought-date/<int:pk>/update/", SSRThoughtDateUpdateView.as_view(), name = "ssr-thought-date-update"),
    path("thought-date/<int:pk>/delete/", SSRThoughtDateDeleteView.as_view(), name = "ssr-thought-date-delete"),

    path("actions/", SSRActionListView.as_view(), name="ssr-action-list"),
    path("action/create/", SSRActionCreateView.as_view(), name="ssr-action-create"),
    path("action/<int:pk>/", SSRActionDetailView.as_view() , name="ssr-action-detail"),
    path("action/<pk>/update/", SSRActionUpdateView.as_view(), name="ssr-action-update"),
    path("action/<pk>/delete/", SSRActionDeleteView.as_view(), name="ssr-action-delete"),

    path("charts/", SSRChartsView.as_view(), name="ssr-charts"),
    path("most-relevant-thoughts/", ssr_most_relevant_thoughts_view, name = "ssr-most-relevant-thoughts"),
    path("action/chart/emotion", ssr_action_emotion_chart_view, name="ssr-action-emotion-chart"),
    path("action-date/chart/sad-intensity/today/", ssr_actiondate_sad_intensity_today_chart_view, name="ssr-action-date-sad-intensity-today-chart"),
    path("action-date/chart/sad-intensity/last-30-days-chart/", ssr_actiondate_sad_intensity_last_30_days_view, name="ssr-action-date-sad-intensity-last-30-days-chart"),

]
