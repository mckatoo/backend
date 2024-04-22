from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from pages.models import Pages


@require_http_methods(["GET"])
def get_pages(_, page):
    data = get_object_or_404(Pages, slug=page)
    json = data.__json__()

    return JsonResponse(json)
