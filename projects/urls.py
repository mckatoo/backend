from django.urls import path

from pages.views import list_projects

urlpatterns = [path("", list_projects, name='list_projects')]
