from django_filters import rest_framework as filters


class IsOwnerFilterBackend(filters.DjangoFilterBackend):
    """
    Filter that only allows users to get their own objects
    """
    def filter_queryset(self, request, queryset, view):
        user_id = request.user.id
        print(user_id)
        return queryset.filter(user=user_id)
