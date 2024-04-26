from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from skills.models import Skills
from utils.to_json import queryset_to_json


@require_http_methods(["GET"])
def list_skills(request):
    skills = Skills.objects.all()
    json_data = queryset_to_json(skills)

    return HttpResponse(json_data, content_type="application/json")
