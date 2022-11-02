from rest_framework import serializers
from employees import models


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = "__all__"


# class AddEmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Employees
#         fields = ['first_name', "last_name", "description", "avatar"]