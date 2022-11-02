from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from photoblog import serializers
from photoblog import models
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes


@swagger_auto_schema(operation_description="This endpoint returns every gallery", method="GET")
@api_view(["GET"])
def get(request):
    data = models.Gallery.objects.all()

    serializer = serializers.GallerySerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(operation_description="This endpoint returns gallery based on id", method="GET")
@api_view(["GET"])
def getById(request, pk):
    data = models.Gallery.objects.get(pk=pk)

    serializer = serializers.GallerySerializer(data, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(operation_description="This endpoint deletes gallery item based on id", method="DELETE")
@permission_classes([IsAdminUser])
@api_view(["DELETE"])
def delete(request, pk):
    data = models.Gallery.objects.get(pk=pk)
    image = data.image.path
    if data:
        if data.delete():
            models.img_delete(image)
            return Response(f"Gallery item with id: {pk} deleted successfully.", status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint adds a new Gallery item.", method="POST", request_body=serializers.GallerySerializer)
@permission_classes([IsAdminUser])
@api_view(["POST"])
@parser_classes([MultiPartParser])
def post(request):
    serializer = serializers.GallerySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response("Gallery item added successfully", status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint updates a gallery item based on id.",
                     method="PUT", request_body=serializers.GallerySerializer)
@permission_classes([IsAdminUser])
@api_view(["PUT"])
@parser_classes([MultiPartParser])
def put(request, pk):
    data = models.Gallery.objects.get(pk=pk)
    image = data.image.path
    serializer = serializers.GallerySerializer(data, data=request.data)

    if serializer.is_valid():
        if serializer.save():

            models.img_delete(image)

            return Response(f"Gallery item with id: {pk} was updated successfully", status=status.HTTP_200_OK)
    return Response(f"Something went wrong while deleting Gallery item with the id: {pk}", status=status.HTTP_400_BAD_REQUEST)