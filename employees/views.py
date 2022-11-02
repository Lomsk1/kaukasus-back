from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAdminUser
from employees import models
from employees import serializers
from rest_framework import status
from rest_framework.parsers import MultiPartParser

@swagger_auto_schema(operation_description="This endpoint return every employee", method="GET")
@api_view(['GET'])
def get(request):
    employees = models.Employees.objects.all()
    serializer = serializers.EmployeesSerializer(employees, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns employee based on the id", method="GET")
@api_view(['GET'])
def byid(request, pk):
    employee = models.Employees.objects.get(pk=pk)
    serializer = serializers.EmployeesSerializer(employee, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint adds new employee", method="POST", request_body=serializers.EmployeesSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser])
def post(request):
    employee = serializers.EmployeesSerializer(data=request.data)

    if employee.is_valid():
        employee.save()
        return Response("Employee has added successfully", status=status.HTTP_200_OK)

    return Response(employee.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint deletes an employee based on id.", method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete(request, pk):
    employee = models.Employees.objects.get(pk=pk)
    image = employee.avatar.path

    if employee:
        if employee.delete():
            employee.img_delete(image)
            return Response("Employee was deleted successfully", status=status.HTTP_200_OK)
    return Response("Employee with that id doesn't exist.", status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint updates an employee based on id.", method="PUT", request_body=serializers.EmployeesSerializer)
@api_view(['PUT'])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser])
def put(request, pk):
    employee = models.Employees.objects.get(pk=pk)
    serializer = serializers.EmployeesSerializer(employee, data=request.data)

    image = employee.avatar.path

    if serializer.is_valid():

        if serializer.save():
            employee.img_delete(image)

        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)