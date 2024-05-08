from django.urls import re_path

from projects.views import CreateProject, GetUpdateDeleteProject, ListProjects


urlpatterns = [ 
    re_path("^projects/?$", ListProjects.as_view()),
    re_path("project/?$", CreateProject.as_view()),
    re_path("project/<int:pk>/?$", GetUpdateDeleteProject.as_view()),
]
