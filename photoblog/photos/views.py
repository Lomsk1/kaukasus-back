from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from photoblog import serializers
from photoblog import models
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes

@swagger_auto_schema(operation_description="This endpoint returns every photo-blog item.", method="GET")
@api_view(["GET"])
def get(request):
    photo_blogs = models.Photos.objects.all()
    serializer = serializers.PhotoSerializer(photo_blogs, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint returns every photo item based on gallery id.", method="GET")
@api_view(["GET"])
def getAllPhotosById(request, gallery_pk):
    data = models.Photos.objects.filter(gallery_id=gallery_pk)

    serializer = serializers.PhotoSerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)



@swagger_auto_schema(operation_description="This endpoint returns a photo-blog item based on id.", method="GET")
@api_view(['GET'])
def byid(request, pk):
    photo_blog = models.Photos.objects.get(pk=pk)
    serializer = serializers.PhotoBlogSerializer(photo_blog, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint creates new photo-blog item.", method="POST", request_body=serializers.PhotoSerializer)
@permission_classes([IsAdminUser])
@api_view(["POST"])
@parser_classes([MultiPartParser])
def post(request):
    serializer = serializers.PhotoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({"saved": False}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint updates photo-blog item based on id.", method="PUT", request_body=serializers.PhotoSerializer)
@permission_classes([IsAdminUser])
@api_view(['PUT'])
@parser_classes([MultiPartParser])
def put(request, pk):
    photoblog = models.Photos.objects.get(pk=pk)
    serializer = serializers.PhotoSerializer(photoblog, data=request.data)

    image = photoblog.image.path

    if serializer.is_valid():

        if serializer.save():
            models.img_delete(image)

        return Response(serializer.data)
    return Response(serializer.errors)


@swagger_auto_schema(operation_description="This endpoint deletes photo-blog item based on id.", method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete(request, pk):
    photoblog = models.Photos.objects.get(pk=pk)

    image = photoblog.image.url

    if photoblog:
        if photoblog.delete():
            models.img_delete(image)

            return Response("photo-blog item was successfully deleted!", status=status.HTTP_200_OK)
        else:
            return Response("Photo blog with that id doesn't exist", status=status.HTTP_400_BAD_REQUEST)

