from rest_framework.views import APIView, Response
from pages.models import Pages
from pages.serializers import PageSerializer


class GetPage(APIView):
    def get(self, _, page):
        data = PageSerializer(Pages.objects.get(slug=page)).data
        return Response(data)
