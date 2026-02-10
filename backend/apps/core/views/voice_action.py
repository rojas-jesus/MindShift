from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import VoiceActionEntry
from ..serializers import VoiceActionEntrySerializer


class VoiceActionEntryCreateView(CreateAPIView):
    queryset = VoiceActionEntry.objects.all()
    serializer_class = VoiceActionEntrySerializer
    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        print(f"DEBUG: VoiceActionEntryCreateView hit at {request.path}")
        return super().dispatch(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


