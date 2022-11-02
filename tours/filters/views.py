from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tours import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint filters tours by tag it.", method="GET")
@api_view(["GET"])
def filterTourByTag(request, tag_id):
    tag = models.Tags.objects.get(pk=tag_id)

    tours = models.Tour.objects.filter(tag=tag)

    serializer = serializers.TourSerializer(tours, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="POST",
                     operation_description="This endpoint will return all of the tours with dates between from and start. ",
                     request_body=serializers.DateFilterSerializer
                    )
@api_view(["POST"])
def filterByDate(request):
    fr = request.data.get("startDate")
    to = request.data.get("endDate")

    tour_ids = models.Booking.objects.filter(startDate__gte=fr, endDate__lte=to).values("tour").distinct()
    tours = []


    for tour_id in tour_ids:
        tours.append(models.Tour.objects.get(pk=tour_id['tour']))


    serializer = serializers.TourSerializer(tours, many=True)



    return Response(serializer.data, status=status.HTTP_200_OK)
