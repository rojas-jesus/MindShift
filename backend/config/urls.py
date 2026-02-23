# Triggering reload for new token serializer
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def test_connection(request):
    return HttpResponse("Backend connection OK")

urlpatterns = [
    path('api/test/', test_connection),
    path('admin/', admin.site.urls),
    path("home/", include("apps.homepage.urls")),
    path("api/", include("apps.core.urls.api_urls")),
    path("ssr/", include("apps.core.urls.ssr_urls")),
    path("account/", include("apps.account.urls")),
    path('', include('django_prometheus.urls')),

    # OpenAPI schema & docs
    # path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # path(
    #     "api/schema/swagger/",
    #     SpectacularSwaggerView.as_view(url_name="schema"),
    #     name="swagger-ui",
    # ),
    # path(
    #     "api/schema/redoc/",
    #     SpectacularRedocView.as_view(url_name="schema"),
    #     name="redoc",
    # ),
]
