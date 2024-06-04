from django.shortcuts import render

from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.decorators import action

from api.models import Employee

from api.serializers import EmployeeSerializer, TaskSerializer

# Create your views here.

class EmployeeViewSetView(viewsets.ModelViewSet):

   serializer_class=EmployeeSerializer

   queryset=Employee.objects.all()

   @action(methods=["POST"],detail=True)
   def add_task(self,request,*args, **kwargs):

      id=kwargs.get("pk")

      employee_obj=Employee.objects.get(id=id)

      serializer_instance=TaskSerializer(data=request.data) #deseralizer

      if serializer_instance.is_valid():

         serializer_instance.save(employee_object=employee_obj)

         return Response(data=serializer_instance.data)
      
      else:

         return Response(data=serializer_instance.errors)

