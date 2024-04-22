from django.contrib import admin
from django.http.response import JsonResponse
from django.urls import include, path


def get_version(request):
    # version = importlib.metadata.version("backend")
    return JsonResponse({"version": "1.0"})


urlpatterns = [
    path("projects/", include("projects.urls")),
    path("admin/", admin.site.urls),
    path("", get_version, name="version"),
    path("", include("pages.urls")),
]
