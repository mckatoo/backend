from django.urls import path
from skills.views import list_skills


urlpatterns = [path("", list_skills, name="list_skills")]
