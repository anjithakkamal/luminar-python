from rest_framework import serializers

from api.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):

    user_object=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Expense

        fields="__all__"

        read_only_fields=["id","created_date","user_object"]