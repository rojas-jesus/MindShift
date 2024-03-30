from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from ..models import Environment
from ..serializers import EnvironmentSerializer


# Environment views
class EnvironmentsListView(ListAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class EnvironmentCreateView(CreateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class EnvironmentRetrieveView(RetrieveAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    lookup_field = "id"


class EnvironmentUpdateView(UpdateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    lookup_field = "id"
    fields = ("id", "name", "description")


class EnvironmentDeleteView(DestroyAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    lookup_field = "id"

