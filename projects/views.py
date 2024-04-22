from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

from projects.models import Projects

from utils.to_json import queryset_to_json


@require_http_methods(["GET"])
def list_projects(request):
    projects = Projects.objects.all()
    json_data = queryset_to_json(projects)

    return HttpResponse(json_data, content_type="application/json")
