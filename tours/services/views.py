from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tours import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns every Services", method="GET")
@api_view(["GET"])
def get(request):

    data = models.Services.objects.all()

    serializer = serializers.ServicesSerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(operation_description="This endpoint returns Service based on id", method="GET")
@api_view(["GET"])
def getById(request, pk):
    service = models.Services.objects.get(pk=pk)
    serviceSerializer = serializers.ServicesSerializer(service, many=False).data

    return Response(serviceSerializer, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint creates new Service for a tour.", method="POST", request_body=serializers.ServicesSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
def post(request):
    service = serializers.ServicesSerializer(data=request.data)

    if service.is_valid():
        service.save()
        return Response("Service has added successfully", status=status.HTTP_200_OK)

    return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint updates a service.", method="PUT", request_body=serializers.ServicesSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def put(request, pk):
    service = models.Services.objects.get(pk=pk)
    serializer = serializers.ServicesSerializer(service, data=request.data)

    if serializer.is_valid():
        if serializer.save():
            return Response("Service has been updated successfully", status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint deletes a Service.", method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete(request, pk):
    service = models.Services.objects.get(pk=pk)
    if service:
        if service.delete():
            return Response("Service deleted successfully", status.HTTP_200_OK)
    return Response("Error While deleting service", status.HTTP_404_NOT_FOUND)