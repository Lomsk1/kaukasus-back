from rest_framework import serializers
from country_info import models

class CountryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CountryInfo
        fields = "__all__"


class CountryInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CountryInfo
        fields = [
            "title",
            "description"
        ]