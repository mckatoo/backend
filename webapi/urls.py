from django.contrib import admin
from django.http.response import JsonResponse
from django.urls import include, path
from django.conf.urls.static import static


from webapi import settings


def get_version(request):
    # version = importlib.metadata.version("backend")
    return JsonResponse({"version": "1.0"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    path("", include("projects.urls")),
    path("", include("skills.urls")),
    path("", include("pages.urls")),
    path("", get_version, name="version"),
    path("summernote/", include("django_summernote.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
