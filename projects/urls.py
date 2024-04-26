from django.urls import path

from projects.views import CreateProject, GetUpdateDeleteProject, ListProjects


urlpatterns = [
    path("projects/", ListProjects.as_view()),
    path("project/", CreateProject.as_view()),
    path("project/<int:pk>", GetUpdateDeleteProject.as_view()),
]
