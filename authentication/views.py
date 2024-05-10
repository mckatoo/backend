from django.conf import settings
import requests
from rest_framework.authentication import (
    BasicAuthentication,
)
from rest_framework.decorators import (
    api_view,
    authentication_classes,
)
from rest_framework.views import Response


@api_view(["POST"])
@authentication_classes([BasicAuthentication])
def sign_in(request):
    url = f"{settings.KEYCLOAK_SERVER_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token"
    response = requests.post(
        url=url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "client_id": settings.KEYCLOAK_CLIENT_ID,
            "username": request.data["username"],
            "password": request.data["password"],
            "grant_type": "password",
        },
    )

    if not response.ok:
        return Response(response.reason, status=response.status_code)

    data = response.json()
    return Response(
        {
            "accessToken": data["access_token"],
            "refreshToken": data["refresh_token"],
        }
    )


@api_view(["POST"])
def sign_out(_):
    return Response()


@api_view(["GET"])
def verify(_):
    return Response()


@api_view(["POST"])
def refresh(_):
    return Response()
