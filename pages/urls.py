from django.urls import path

from pages.views import CreatePage, GetUpdateDeletePage

urlpatterns = [
    path("page/<slug:page>/", GetUpdateDeletePage.as_view()),
    path("page/", CreatePage.as_view()),
]
