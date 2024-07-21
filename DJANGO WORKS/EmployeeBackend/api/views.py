from django.shortcuts import render

from rest_framework import viewsets

from api.models import Employee

from api.serializers import EmployeeSerializers

# Create your views here.

class EmployeeViewSetView(viewsets.ModelViewSet):

    serializer_class=EmployeeSerializers

    queryset=Employee.objects.all()

    model=Employee
