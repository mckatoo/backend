from django.urls import re_path

from authentication.views import sign_in, sign_out, verify


urlpatterns = [
    re_path("^sign-in/?$", sign_in),
    re_path("^sign-out/?$", sign_out),
    re_path("^verify-token/?$", verify),
    re_path("^refresh/?$", verify),
]
