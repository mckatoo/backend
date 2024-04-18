from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from pages.models import Pages


@require_http_methods(["GET"])
def get_pages(request, page):
    data = get_object_or_404(Pages, url=page)

    return JsonResponse(model_to_dict(data), safe=False)
