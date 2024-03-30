from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated

from ..models import Facilitator
from ..serializers import FacilitatorSerializer


# Facilitator views
class FacilitatorsListView(ListAPIView):
    queryset = Facilitator.objects.all()
    serializer_class = FacilitatorSerializer


class FacilitatorCreateView(CreateAPIView):
    queryset = Facilitator.objects.all()
    serializer_class = FacilitatorSerializer
    permission_classes = [IsAuthenticated]


class FacilitatorRetrieveView(RetrieveAPIView):
    queryset = Facilitator.objects.all()
    serializer_class = FacilitatorSerializer
    lookup_field = "id"


class FacilitatorUpdateView(UpdateAPIView):
    queryset = Facilitator.objects.all()
    serializer_class = FacilitatorSerializer
    lookup_field = "id"
    fields = ("id", "name", "description")


class FacilitatorDeleteView(DestroyAPIView):
    queryset = Facilitator.objects.all()
    serializer_class = FacilitatorSerializer
    lookup_field = "id"

