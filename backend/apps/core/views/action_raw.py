from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import ActionRaw
from ..serializers import ActionRawSerializer


class ActionRawCreateView(CreateAPIView):
    queryset = ActionRaw.objects.all()
    serializer_class = ActionRawSerializer
    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        print(f"DEBUG: ActionRawCreateView hit at {request.path}")
        return super().dispatch(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


