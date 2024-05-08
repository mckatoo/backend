from django.urls import re_path

from mailer.views import send


urlpatterns = [re_path("^mailer/?$", send)]
