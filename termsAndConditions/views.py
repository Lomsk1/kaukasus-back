from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from termsAndConditions import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns terms and conditions", method="GET")
@api_view(["GET"])
def get(request):

    data = models.TermsAndConditions.objects.all()
    serializer = serializers.TermsAndConditionsSerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="This endpoint updates terms and conditions",
                     method="PUT", request_body=serializers.TermsAndConditionsSerializer)
@permission_classes([IsAdminUser])
@api_view(["PUT"])
def put(request, pk):
    data = models.TermsAndConditions.objects.get(pk=pk)

    serializer = serializers.TermsAndConditionsSerializer(data, data=request.data)

    if serializer.is_valid():
        if serializer.save():

            return Response(serializer.data, status=status.HTTP_200_OK)