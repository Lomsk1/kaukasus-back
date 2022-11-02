from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tours import models, serializers
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser

@swagger_auto_schema(operation_description="This endpoint returns tour days based on tour_id.", method="GET")
@api_view(["GET"])
def getTourDays(request, tour_id):
    tour = models.Tour.objects.get(pk=tour_id)
    tour_days = models.TourDays.objects.filter(tour=tour)

    serializer = serializers.TourDaysSerializer(tour_days, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint returns singular tour day based on day_id.", method="GET")
@api_view(["GET"])
def getTourDaysById(request, day_id):
    tour_day = models.TourDays.objects.get(pk=day_id)
    serializer = serializers.TourDaysSerializer(tour_day, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint deletes tour day based on day_id.", method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteTourDay(request, day_id):
    tour_day = models.TourDays.objects.get(pk=day_id)

    image = tour_day.image.path

    if tour_day:
        if tour_day.delete():
            models.img_delete(image)
            return Response("Tour day deleted successfully.")
    return Response("Tour day with that id doesn't exist.")


@swagger_auto_schema(operation_description="This Endpoint creates new tour day", method="POST", request_body=serializers.TourDaysSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser])
def postTourDay(request):
    tour_day = serializers.TourDaysSerializer(data=request.data)

    if tour_day.is_valid():
        tour_day.save()
        return Response("Tour_day added successfully", status=status.HTTP_200_OK)
    return Response(tour_day.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint updates a tour day based on id", method="PUT", request_body=serializers.TourDaysSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser])
def putTourDay(request, day_id):
    tour_day = models.TourDays.objects.get(pk=day_id)
    image = tour_day.image.path

    serializer = serializers.TourDaysSerializer(tour_day, data=request.data)

    if serializer.is_valid():
        if serializer.save():
            models.img_delete(image)
            return Response("Tour day successfully updated", status=status.HTTP_200_OK)
        else:
            return Response("Something went wrong")