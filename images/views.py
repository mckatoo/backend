from rest_framework.decorators import APIView
from rest_framework.exceptions import status
from rest_framework.views import Response
import cloudinary
import cloudinary.uploader
import cloudinary.api

from decouple import config

cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUDNAME"),
    api_key=config("CLOUDINARY_APIKEY"),
    api_secret=config("CLOUDINARY_APISECRET"),
    secure=True,
)
folder = config("CLOUDINARY_FOLDER")


class GetUploadDeleteImage(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        image = request.FILES["file"]
        response = cloudinary.uploader.upload(image, folder=folder)

        return Response(
            {
                "url": response['secure_url'],
                "publicId": response['public_id'],
            },
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)
