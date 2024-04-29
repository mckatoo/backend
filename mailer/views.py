from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.views import Response, status

from mailer.serializer import MailerSerializer
from webapi.settings import EMAIL_HOST_USER
from decouple import config


@api_view(["POST"])
def send(request):
    serializer = MailerSerializer(
        data={"_from": request.data["from"], "message": request.data["message"]}
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    send_mail(
        str(config("EMAIL_SUBJECT_PREFIX")) + "CONTACT",
        dict(serializer.data)["message"],
        dict(serializer.data)["_from"],
        [str(EMAIL_HOST_USER)],
        fail_silently=False,
        html_message=dict(serializer.data)["message"],
    )
    return Response(dict(serializer.data)["id"], status=status.HTTP_201_CREATED)
