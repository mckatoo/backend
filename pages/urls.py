from django.urls import path

from pages.views import GetUpdateDeletePage, create_page

urlpatterns = [
    path("page/", create_page),
    path("<slug:page>/", GetUpdateDeletePage.as_view()),
]
