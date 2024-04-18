from django.urls import path

from pages.views import get_pages

urlpatterns = [path("<slug:page>/", get_pages, name='pages')]
