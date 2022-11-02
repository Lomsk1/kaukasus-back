from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tours import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(operation_description="This endpoint returns tags.", method="GET")
@api_view(["GET"])
def get(request):
    tags = models.Tags.objects.all()

    serializer = serializers.TagSerializer(tags, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint returns tag based on id", method="GET")
@api_view(["GET"])
def getById(request, pk):

    tag = models.Tags.objects.get(id=pk)

    serializer = serializers.TagSerializer(tag, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([IsAdminUser])
@swagger_auto_schema(operation_description="This endpoint creates new tag.", method="POST", request_body=serializers.TagSerializer)
@api_view(["POST"])
def post(request):
    tag = serializers.TagSerializer(data=request.data)

    if tag.is_valid():
        tag.save()
        return Response("Tag has been added successfully", status=status.HTTP_200_OK)

    return Response(tag.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAdminUser])
@swagger_auto_schema(operation_description="This endpoint updates a tag.", method="PUT", request_body=serializers.TagSerializer)
@api_view(["PUT"])
def put(request, pk):

    tag = models.Tags.objects.get(pk=pk)
    serializer = serializers.TagSerializer(tag, data=request.data)

    if serializer.is_valid():
        if serializer.save():
            return Response("Tag has been updated successfully", status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
@swagger_auto_schema(operation_description="This endpoint deletes a tag.", method="DELETE")
@api_view(["DELETE"])
def delete(request, pk):
    tag = models.Tags.objects.get(pk=pk)

    if tag:
        if tag.delete():
            return Response("Tag deleted successfully", status.HTTP_200_OK)
    return Response("Tag with this id doesn't exist", status.HTTP_404_NOT_FOUND)