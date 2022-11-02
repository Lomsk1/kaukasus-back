from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tours import models, serializers
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser


@swagger_auto_schema(operation_description="This endpoint returns every tour", method="GET")
@api_view(["GET"])
def getTour(request):

    data = models.Tour.objects.all()

    serializer = serializers.TourSerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint returns tour and all associated bookings based on tour_id", method="GET")
@api_view(["GET"])
def getTourById(request, pk):
    tour = models.Tour.objects.get(pk=pk)
    bookings = tour.booking_set
    highlights = tour.highlight_set

    try:
        services = models.Services.objects.get(tour=tour)
    except models.Services.DoesNotExist:
        services = []
    bookingSerializer = serializers.BookingSerializer(bookings, many=True).data
    tourSerializer = serializers.TourSerializer(tour, many=False).data
    highLightSerializer = serializers.HighlightSerializer(highlights, many=True).data
    servicesSerializer = serializers.ServicesSerializer(services, many=False).data

    data = {
        "highlights": highLightSerializer,
        "Tour": tourSerializer,
        "bookings": bookingSerializer,
        "services": servicesSerializer
    }

    return Response(data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint filters out tours based on country", method="GET")
@api_view(["GET"])
def getTourByCountry(request, country):
    data = models.Tour.objects.filter(countryName=country)

    serializer = serializers.TourSerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint creates new tour.", method="POST", request_body=serializers.TourSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser])
def postTour(request):
    tour = serializers.TourSerializer(data=request.data)

    if tour.is_valid():
        tour.save()
        return Response("Tour has added successfully", status=status.HTTP_200_OK)

    return Response(tour.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint updates a tour.", method="PUT", request_body=serializers.TourSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser])
def putTour(request, pk):
    tour = models.Tour.objects.get(pk=pk)
    image = tour.image.path
    serializer = serializers.TourSerializer(tour, data=request.data)

    if serializer.is_valid():
        if serializer.save():
            models.img_delete(image)

            return Response("Tour has been updated successfully", status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint deletes a tour.", method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteTour(request, pk):
    tour = models.Tour.objects.get(pk=pk)
    image = tour.image.path

    if tour:
        if tour.delete():
            models.img_delete(image)

            return Response("Tour deleted successfully", status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("tour with this id doesn't exist", status.HTTP_404_NOT_FOUND)