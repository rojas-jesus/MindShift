from django.urls import path, include
from .ssr_urls import urlpatterns as ssr_urls
from .api_urls import urlpatterns as api_urls  

app_name = "core"

urlpatterns = [
    path("ssr/", include(ssr_urls)),
    path("api/", include(api_urls)),
]