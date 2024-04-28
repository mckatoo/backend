from django.urls import path

from pages.views import GetPage

urlpatterns = [
    path("<slug:page>/", GetPage.as_view()),
]
