import imp
from pyexpat import model
from rest_framework import serializers

from api.models import Employee

class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:

        model=Employee

        fields="__all__"

        read_only_fields=["id"]