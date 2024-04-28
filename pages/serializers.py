from rest_framework import serializers

from images.serializers import ImageSerializer
from pages.models import Pages


class PageSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)

    class Meta:
        model = Pages
        fields = "__all__"
