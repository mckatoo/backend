from django.urls import path, re_path

from projects.views import CreateProject, GetUpdateDeleteProject, ListProjects


urlpatterns = [
    path("project/<int:pk>", GetUpdateDeleteProject.as_view()),
    re_path("^project/?$", CreateProject.as_view()),
    re_path("^projects/?$", ListProjects.as_view()),
]
