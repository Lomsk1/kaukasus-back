from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tours import models, serializers
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns every booking item", method="GET")
@api_view(["GET"])
def get(request):
    data = models.Booking.objects.all()

    serializer = serializers.BookingSerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint returns every booking based on id", method="GET")
@api_view(["GET"])
def getById(request, pk):
    data = models.Booking.objects.get(pk=pk)

    serializer = serializers.BookingSerializer(data, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="this endpoint creates new Booking item", method="POST", request_body=serializers.BookingSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser])

def post(request):
    booking = serializers.BookingSerializer(data=request.data)

    if booking.is_valid():
        booking.save()
        return Response("Booking has added successfully", status=status.HTTP_200_OK)

    return Response(booking.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint updates Booking item.", method="PUT", request_body=serializers.BookingSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser])
def put(request, pk):
    booking = models.Booking.objects.get(pk=pk)
    serializer = serializers.BookingSerializer(booking, data=request.data)

    if serializer.is_valid():
        if serializer.save():

            return Response("Booking has updated successfully", status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint deletes a Booking item .", method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete(request, pk):
    booking = models.Booking.objects.get(pk=pk)

    if booking:
        if booking.delete():
            return Response("Booking has been successfully deleted", status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("tour with this id doesn't exist", status.HTTP_404_NOT_FOUND)



@swagger_auto_schema(operation_description="This endpoint returns all bookings associated to the tour .", method="GET")
@api_view(["GET"])
def getByTour(request, tour_id):
    tour = models.Tour.objects.get(pk=tour_id)

    bookings = tour.booking_set

    serializer = serializers.BookingSerializer(bookings, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
