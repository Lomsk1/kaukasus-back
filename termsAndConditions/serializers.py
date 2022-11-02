from rest_framework import serializers
from termsAndConditions import models

class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TermsAndConditions
        fields = "__all__"
