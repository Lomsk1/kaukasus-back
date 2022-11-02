from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tours import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(operation_description="This endpoint returns single room.", method="GET")
@api_view(["GET"])
def get(request):
    data = models.SingleRoom.objects.all()

    serializer = serializers.SingleRoomSerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAdminUser])
@swagger_auto_schema(operation_description="This endpoint updates a single room.", method="PUT", request_body=serializers.SingleRoomSerializer)
@api_view(["PUT"])
def put(request, pk):
    data = models.SingleRoom.objects.get(pk=pk)
    serializer = serializers.SingleRoomSerializer(data, data=request.data)
    if serializer.is_valid():
        if serializer.save():
            return Response("single room has been updated successfully", status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
