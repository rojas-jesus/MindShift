from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import ThoughtRaw
from ..serializers import ThoughtRawSerializer

class ThoughtRawCreateView(CreateAPIView):
    queryset = ThoughtRaw.objects.all()
    serializer_class = ThoughtRawSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

