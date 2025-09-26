from django.urls import path
from .views import (
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


        # ThoughtListView, 
        # ThoughtCreateView, 
        # ThoughtDetailView,
        # ThoughtUpdateView,
        # ThoughtDeleteView,
        # ThoughtDateListView,
        # ThoughtDateCreateView,
        # ThoughtDateDetailView,
        # ThoughtDateUpdateView,
        # ThoughtDateDeleteView,
        # ActionListView,
        # ActionCreateView, 
        # ActionDetailView,
        # ActionUpdateView,
        # ActionDeleteView,

        FacilitatorListView,
        FacilitatorCreateView,
        FacilitatorRetrieveView,
        FacilitatorUpdateView,
        FacilitatorDeleteView,
        EnvironmentListView,
        EnvironmentCreateView,
        EnvironmentRetrieveView,
        EnvironmentUpdateView,
        EnvironmentDeleteView,

        UserThoughtsTextView,
        AIThoughtsAnalysisView, 
        )


app_name = "core"

urlpatterns = [

    # SSR
    path("ssr/home/", ssr_home, name = "ssr-home" ),

    path("ssr/thoughts/", SSRThoughtListView.as_view(), name = "ssr-thought-list"),
    path("ssr/thought/create/", SSRThoughtCreateView.as_view(), name = "ssr-thought-create"),
    path("ssr/thought/<int:pk>/", SSRThoughtDetailView.as_view(), name = "ssr-thought-detail"),
    path("ssr/thought/<int:pk>/update/", SSRThoughtUpdateView.as_view(), name="ssr-thought-update"),
    path("ssr/thought/<int:pk>/delete/", SSRThoughtDeleteView.as_view(), name="ssr-thought-delete"),

    path("ssr/thought-dates/", SSRThoughtDateListView.as_view(), name = "ssr-thought-date-list"),
    path("ssr/thought-date/create/", SSRThoughtDateCreateView.as_view(), name = "ssr-thought-date-create"),
    path("ssr/thought-date/<int:pk>/", SSRThoughtDateDetailView.as_view(), name = "ssr-thought-date-detail"),
    path("ssr/thought-date/<int:pk>/update/", SSRThoughtDateUpdateView.as_view(), name = "ssr-thought-date-update"),
    path("ssr/thought-date/<int:pk>/delete/", SSRThoughtDateDeleteView.as_view(), name = "ssr-thought-date-delete"),

    path("ssr/actions/", SSRActionListView.as_view(), name="ssr-action-list"),
    path("ssr/action/create/", SSRActionCreateView.as_view(), name="ssr-action-create"),
    path("ssr/action/<int:pk>/", SSRActionDetailView.as_view() , name="ssr-action-detail"),
    path("ssr/action/<pk>/update/", SSRActionUpdateView.as_view(), name="ssr-action-update"),
    path("ssr/action/<pk>/delete/", SSRActionDeleteView.as_view(), name="ssr-action-delete"),

    path("ssr/charts/", SSRChartsView.as_view(), name="ssr-charts"),
    path("ssr/most-relevant-thoughts/", ssr_most_relevant_thoughts_view, name = "ssr-most-relevant-thoughts"),
    path("ssr/action/chart/emotion", ssr_action_emotion_chart_view, name="ssr-action-emotion-chart"),
    path("ssr/action-date/chart/sad-intensity/today/", ssr_actiondate_sad_intensity_today_chart_view, name="ssr-action-date-sad-intensity-today-chart"),
    path("ssr/action-date/chart/sad-intensity/last-30-days-chart/", ssr_actiondate_sad_intensity_last_30_days_view, name="ssr-action-date-sad-intensity-last-30-days-chart"),


    # Api
    # path("thoughts/", ThoughtListView.as_view(), name = "thought-list"),

    path("facilitators/", FacilitatorListView.as_view(), name="facilitator-list"),
    path("facilitator/create/", FacilitatorCreateView.as_view(), name="facilitator-create"),
    path("facilitator/<uuid:id>/", FacilitatorRetrieveView.as_view(), name="facilitator-retrieve"),
    path("facilitator/<uuid:id>/update/", FacilitatorUpdateView.as_view(), name="facilitator-update"),
    path("facilitator/<uuid:id>/delete/", FacilitatorDeleteView.as_view(), name="facilitator-delete"),

    path("environments/", EnvironmentListView.as_view(), name="environment-list"),
    path("environment/create/", EnvironmentCreateView.as_view(), name="environment-create"),
    path("environment/<uuid:id>/", EnvironmentRetrieveView.as_view(), name="environment-retrieve"),
    path("environment/<uuid:id>/update/", EnvironmentUpdateView.as_view(), name="environment-update"),
    path("environment/<uuid:id>/delete/", EnvironmentDeleteView.as_view(), name="environment-delete"),

    path("ai/user-thoughts-text/", UserThoughtsTextView.as_view(), name="ai-user-thoughts-text"), # refactor later
    path("ai/thoughts-analysis/", AIThoughtsAnalysisView.as_view(), name="ai-thoughts-analysis")
]
