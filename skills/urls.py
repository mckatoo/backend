from django.urls import path

from skills.views import CreateSkill, GetUpdateDeleteSkill, ListSkills


urlpatterns = [
    path("skill/", CreateSkill.as_view()),
    path("skill/<int:pk>", GetUpdateDeleteSkill.as_view()),
    path("skills/", ListSkills.as_view()),
]
