from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated 

from ..models import Environment
from ..serializers import EnvironmentSerializer
from ..filters import IsOwnerFilterBackend

class EnvironmentListView(ListAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (IsOwnerFilterBackend,)

class EnvironmentCreateView(CreateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EnvironmentRetrieveView(RetrieveAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (IsOwnerFilterBackend,)
    lookup_field = "id"

class EnvironmentUpdateView(UpdateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (IsOwnerFilterBackend,)
    lookup_field = "id"

class EnvironmentDeleteView(DestroyAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (IsOwnerFilterBackend,)
    lookup_field = "id"
