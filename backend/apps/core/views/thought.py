from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from ..models import Thought
from ..serializers import ThoughtSerializer
from ..filters import IsOwnerFilterBackend

class ThoughtListView(ListAPIView):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (IsOwnerFilterBackend,)

class ThoughtCreateView(CreateAPIView):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ThoughtRetrieveView(RetrieveAPIView):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (IsOwnerFilterBackend,)
    lookup_field = "id"

class ThoughtUpdateView(UpdateAPIView):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (IsOwnerFilterBackend,)
    lookup_field = "id"

class ThoughtDeleteView(DestroyAPIView):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (IsOwnerFilterBackend,)
    lookup_field = "id"
