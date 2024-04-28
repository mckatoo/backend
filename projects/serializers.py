from rest_framework import serializers

from projects.models import Projects
from skills.serializers import SkillSerializer


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = "__all__"
