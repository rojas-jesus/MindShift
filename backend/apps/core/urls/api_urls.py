from django.urls import path
from ..views import (
        ThoughtListView, 
        ThoughtCreateView, 
        ThoughtRetrieveView,
        ThoughtUpdateView,
        ThoughtDeleteView,
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
        VoiceThoughtEntryCreateView,
        VoiceActionEntryCreateView,
        )

urlpatterns = [
    path("voice/thought/create/", VoiceThoughtEntryCreateView.as_view(), name="voice-thought-create"),
    path("voice/action/create/", VoiceActionEntryCreateView.as_view(), name="voice-action-create"),

    path("thoughts/", ThoughtListView.as_view(), name = "thought-list"),
    path("thought/create/", ThoughtCreateView.as_view(), name="thought-create"),
    path("thought/<id>/", ThoughtRetrieveView.as_view(), name="thought-retrieve"),
    path("thought/<id>/update/", ThoughtUpdateView.as_view(), name="thought-update"),
    path("thought/<id>/delete/", ThoughtDeleteView.as_view(), name="thought-delete"),

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
    path("ai/thoughts-analysis/", AIThoughtsAnalysisView.as_view(), name="ai-thoughts-analysis"),
]
