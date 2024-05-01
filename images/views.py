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


class PostGetDeleteImage(APIView):
    def post(self, request):
        image = request.FILES["file"]
        try:
            response = cloudinary.uploader.upload(image, folder=folder)
            public_id = response["public_id"]
            secure_url = response["secure_url"]
        except Exception as e:
            raise e

        return Response(
            {
                "url": secure_url,
                "publicId": public_id,
            },
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        public_id = request.data["id"]
        try:
            result = cloudinary.api.resource(public_id)
        except Exception as e:
            if isinstance(e, cloudinary.api.NotFound):
                return Response(status=status.HTTP_404_NOT_FOUND)
            raise e
        return Response({"url": result["url"]})

    def delete(self, request):
        public_id = request.data["id"]
        try:
            cloudinary.uploader.destroy(public_id)
        except Exception as e:
            if isinstance(e, cloudinary.api.NotFound):
                return Response(status=status.HTTP_404_NOT_FOUND)
            raise e
        return Response(status=status.HTTP_204_NO_CONTENT)
