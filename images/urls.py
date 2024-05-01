from django.urls import path

from images.views import PostGetDeleteImage


urlpatterns = [
    path("image/", PostGetDeleteImage.as_view()),
]
