from django.urls import re_path

from pages.views import GetUpdateDeletePage, create_page

urlpatterns = [
    re_path("^page/?$", create_page),
    re_path("^<slug:page>/?$", GetUpdateDeletePage.as_view()),
]
