from django.urls import re_path

from images.views import PostGetDeleteImage


urlpatterns = [
    re_path("^image/?$", PostGetDeleteImage.as_view()),
]
