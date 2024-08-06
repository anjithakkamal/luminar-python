from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from api.models import Expense

from api.serializers import ExpenseSerializer

from rest_framework import permissions,authentication

from rest_framework.viewsets import ModelViewSet

from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class ExpenseViewSetView(ModelViewSet):

    serializer_class=ExpenseSerializer

    queryset=Expense.objects.all()

    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        serializer.save(user_object=self.request.user)

  
  