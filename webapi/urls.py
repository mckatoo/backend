from django.contrib import admin
from django.http.response import JsonResponse
from django.urls import include, path
from django.conf.urls.static import static

from webapi import settings


def get_version(request):
    # version = importlib.metadata.version("backend")
    return JsonResponse({"version": "1.0"})


urlpatterns = [
    path("api/", include("projects.urls")),
    path("api/", include("skills.urls")),
    path("api/", include("mailer.urls")),
    path("api/", include("images.urls")),
    path("api/", include("pages.urls")),
    path("api/", get_version, name="version"),
    path("api/auth/", include("authentication.urls")),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
