from rest_framework.views import APIView, Response, status

from skills.models import Skills
from skills.serializers import SkillSerializer



class ListSkills(APIView):
    def get(self, _):
        data = SkillSerializer(Skills.objects.all(), many=True).data
        return Response(data)


class GetUpdateDeleteSkill(APIView):
    def get(self, _, pk):
        serializer = SkillSerializer(Skills.objects.get(id=pk))
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = SkillSerializer(
            Skills.objects.get(id=pk), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        Skills.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateSkill(APIView):
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
                dict(serializer.data)["id"],
                status=status.HTTP_201_CREATED
                )
