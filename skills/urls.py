from django.urls import re_path

from skills.views import CreateSkill, GetUpdateDeleteSkill, ListSkills


urlpatterns = [
    re_path("^skill/?$", CreateSkill.as_view()),
    re_path("^skill/<int:pk>/", GetUpdateDeleteSkill.as_view()),
    re_path("^skills/?$", ListSkills.as_view()),
]
