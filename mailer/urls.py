from django.urls import path

from mailer.views import send


urlpatterns = [path("mailer/", send)]
