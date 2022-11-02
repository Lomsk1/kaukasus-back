from rest_framework import serializers
from tours import models


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields = "__all__"


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tour
        fields = "__all__"

class TourDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourDays
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"

class DateFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = [
            "startDate",
            "endDate",
        ]

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = "__all__"


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Highlight
        fields = "__all__"

class SingleRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SingleRoom
        fields = "__all__"