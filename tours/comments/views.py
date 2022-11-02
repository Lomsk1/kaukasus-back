from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tours import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(operation_description="This endpoint returns comments.", method="GET")
@api_view(["GET"])
def get(request):
    comments = models.Comments.objects.all()

    serializer = serializers.CommentsSerializer(comments, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint comment based on id", method="GET")
@api_view(["GET"])
def getById(request, pk):

    comment = models.Comments.objects.get(pk=pk)

    serializer = serializers.CommentsSerializer(comment, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint returns all the comments based on the tour_id", method="GET")
@api_view(["GET"])
def getByTour(request, tour_id):

    comments = models.Comments.objects.filter(tour=tour_id)

    serializer = serializers.CommentsSerializer(comments, many=True)

    if serializer:
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAdminUser])
@swagger_auto_schema(operation_description="This endpoint creates new comment", method="POST", request_body=serializers.CommentsSerializer)
@api_view(["POST"])
def post(request):
    comment = serializers.CommentsSerializer(data=request.data)

    if comment.is_valid():
        comment.save()
        return Response("Comment has been added successfully", status=status.HTTP_200_OK)

    return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
@swagger_auto_schema(operation_description="This endpoint updates a comment.", method="PUT", request_body=serializers.CommentsSerializer)
@api_view(["PUT"])
def put(request, pk):

    comment = models.Comments.objects.get(pk=pk)
    serializer = serializers.CommentsSerializer(comment, data=request.data)

    if serializer.is_valid():
        if serializer.save():
            return Response("Comment has been successfully updated", status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
@swagger_auto_schema(operation_description="This endpoint deletes a comment.", method="DELETE")
@api_view(["DELETE"])
def delete(request, pk):
    comment = models.Comments.objects.get(pk=pk)

    serializer = serializers.CommentsSerializer(comment, many=False)

    if comment:
        if comment.delete():
            return Response(["Comment deleted successfully", serializer.data], status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_404_NOT_FOUND)