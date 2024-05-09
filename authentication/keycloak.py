from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import jwt


class KeycloakAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION", "").split("Bearer ")[
                -1
            ]
            algorithm = jwt.get_unverified_header(token)["alg"]
            jwks_url = f"{settings.KEYCLOAK_SERVER_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/certs"
            jwks_client = jwt.PyJWKClient(jwks_url)
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=[algorithm],
                audience="account",
            )
            user = User.objects.get(username=payload["preferred_username"])
            return user, None
        except Exception as e:
            raise exceptions.AuthenticationFailed(e)
