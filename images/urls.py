from django.urls import path

from images.views import GetUploadDeleteImage


urlpatterns = [path("image/", GetUploadDeleteImage.as_view())]
