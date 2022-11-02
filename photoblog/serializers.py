from rest_framework import serializers
from photoblog import models


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photos
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields  = "__all__"