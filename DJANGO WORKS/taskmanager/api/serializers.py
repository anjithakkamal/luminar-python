from rest_framework import serializers

from api.models import Employee, Task

class TaskSerializer(serializers.ModelSerializer):

    employee_object=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Task

        fields="__all__"

        read_only_fields=["id","employee_object"]

class EmployeeSerializer(serializers.ModelSerializer):

    works=TaskSerializer(many=True,read_only=True) #nested serializer

    class Meta:

        model=Employee

        fields=["id","name","department","salary","works"]

