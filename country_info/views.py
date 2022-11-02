from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from country_info import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns every country_info", method="GET")
@api_view(["GET"])
def get(request):
    data = models.CountryInfo.objects.all()
    serializer = serializers.CountryInfoSerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint updates country info",method="PUT", request_body=serializers.CountryInfoUpdateSerializer)
@permission_classes([IsAdminUser])
@api_view(["PUT"])
def put(request, pk):
    data = models.CountryInfo.objects.get(pk=pk)

    serializer = serializers.CountryInfoUpdateSerializer(data, data=request.data)

    if serializer.is_valid():
        if serializer.save():
            return Response(serializer.data, status=status.HTTP_200_OK)