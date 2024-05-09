from rest_framework.decorators import permission_classes
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated

from camel_converter import dict_to_snake

from projects.models import Projects
from projects.serializers import ProjectSerializer


class ListProjects(APIView):
    def get(self, _):
        data = ProjectSerializer(Projects.objects.all(), many=True).data
        return Response(data)


class GetUpdateDeleteProject(APIView):
    def get(self, _, pk):
        serializer = ProjectSerializer(Projects.objects.get(id=pk))
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def patch(self, request, pk):
        serializer = ProjectSerializer(
            Projects.objects.get(id=pk), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
        Projects.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateProject(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProjectSerializer(data=dict_to_snake(request.data))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            dict(serializer.data)["id"], status=status.HTTP_201_CREATED
        )
