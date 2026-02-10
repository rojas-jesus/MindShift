from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import register_view, UserRetrieveView, CurrentUserView, MyTokenObtainPairView

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/register/", register_view, name="register"),
    path('api/user/me/', CurrentUserView.as_view(), name='current-user'),
    path('api/user/<str:username>/', UserRetrieveView.as_view(), name='user-retrieve'),
]
