from rest_framework.views import APIView, Response, status

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

    def patch(self, request, pk):
        serializer = ProjectSerializer(
            Projects.objects.get(id=pk), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        Projects.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateProject(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
                dict(serializer.data)["id"],
                status=status.HTTP_201_CREATED
                )
