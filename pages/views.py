from rest_framework.exceptions import status
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from pages.models import Pages
from pages.serializers import PageSerializer


class GetUpdateDeletePage(APIView):
    def get(self, _, page):
        data = PageSerializer(Pages.objects.get(slug=page)).data
        return Response(data)

    def patch(self, request, pk):
        serializer = PageSerializer(
            Pages.objects.get(id=pk), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        Pages.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_page(request):
    serializer = PageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        dict(serializer.data)["id"], status=status.HTTP_201_CREATED
    )
