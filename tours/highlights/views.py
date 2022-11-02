from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from tours import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns highlights based on tour id.", method="GET")
@api_view(["GET"])
def getHighlights(request, tour_id):
    highlights = models.Highlight.objects.filter(tour=tour_id)

    serializer = serializers.HighlightSerializer(highlights, many=True).data
    return Response(serializer, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint return highlight based on id", method="GET")
@api_view(["GET"])
def getHighlightsById(request, highlight_id):
    highlight = models.Highlight.objects.get(pk=highlight_id)

    serializer = serializers.HighlightSerializer(highlight, many=False).data

    return Response(serializer, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint deletes highlight based on id", method="DELETE")
@api_view(["DELETE"])
def delete(request, highlight_id):
    highlight = models.Highlight.objects.get(pk=highlight_id)

    if highlight.delete():

        return Response("highlight deleted successfully", status=status.HTTP_200_OK)

    return Response("Error While Deleting", status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(operation_description="This endpoint adds a new highlight to a particular tour",
                     request_body=serializers.HighlightSerializer,
                     method="POST")
@api_view(["POST"])
def post(request):
    highlight = serializers.HighlightSerializer(data=request.data)

    if highlight.is_valid():
        highlight.save()
        return Response("highlight has been added successfully.", status=status.HTTP_200_OK)

    return Response(highlight.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(operation_description="This endpoint updates a Highlight.",
                     method="PUT",
                     request_body=serializers.HighlightSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def put(request, pk):
    highlight = models.Highlight.objects.get(pk=pk)
    serializer = serializers.HighlightSerializer(highlight, request.data)

    if serializer.is_valid():
        if serializer.save():
            return Response("Highlight has been updated successfully", status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)