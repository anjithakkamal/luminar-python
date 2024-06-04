from django.shortcuts import render

from django.db.models import Sum

from django.utils import timezone

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import permissions,authentication

from rest_framework.viewsets import ModelViewSet

from api.serializers import ExpenseSerializer, UserSerializer,IncomSerializer

from api.permissions import OwnerOnly

from budget.models import Expense, Income

# Create your views here.

class UserCreationView(APIView):

    def post(self,request,*args, **kwargs):

        serializer_instance=UserSerializer(data=request.data)#create

        if serializer_instance.is_valid():

            serializer_instance.save()#create

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

# =====================================================EXPENSE======================================================================

class ExpenseViewSet(ModelViewSet):

    serializer_class=ExpenseSerializer

    queryset=Expense.objects.all()

    authentication_classes=[authentication.BasicAuthentication]

    # permission_classes=[permissions.IsAuthenticated]

    permission_classes=[OwnerOnly]

    def list(self,request,*args, **kwargs):

        qs=Expense.objects.filter(user_object=request.user)

        serializer_instance=ExpenseSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def perform_create(self, serializer):

        return serializer.save(user_object=self.request.user)

class ExpenseSummaryView(APIView):

    permission_classes=[permissions.IsAuthenticated]

    authentication_classes=[authentication.BasicAuthentication]

    def get(self,request,*args, **kwargs):

        current_month=timezone.now().month

        current_year=timezone.now().year

        all_expense=Expense.objects.filter(

            user_object=request.user,

            created_date__month=current_month,

            created_date__year=current_year
        )

        expense_total=all_expense.values("amount").aggregate(total=Sum("amount"))["total"]

        category_summary=all_expense.values("category").annotate(total=Sum("amount"))

        data={

            "expense_total":expense_total,

            "category_summary":category_summary
        }

        return Response(data=data)

# ==========================================================INCOME==========================================================

class IncomeViewSet(ModelViewSet):

    serializer_class=IncomSerializer

    queryset=Income.objects.all()

    authentication_classes=[authentication.BasicAuthentication]

    # permission_classes=[permissions.IsAuthenticated]

    permission_classes=[OwnerOnly]

    def list(self,request,*args, **kwargs):

        qs=Income.objects.filter(user_object=request.user)

        serilizer_instance=IncomSerializer(qs,many=True)

        return Response(data=serilizer_instance.data)
    
    def perform_create(self, serializer):

        return serializer.save(user_object=self.request.user)

class IncomeSummaryView(APIView):

    permission_classes=[permissions.IsAuthenticated]

    authentication_classess=[authentication.BasicAuthentication]
    
    def get(self,request,*args, **kwargs):

        current_month=timezone.now().month

        current_year=timezone.now().year

        all_incomes=Income.objects.filter(
            
            user_object=request.user,

            created_date__month=current_month,

            created_date__year=current_year
        )

        income_total=all_incomes.values("amount").aggregate(total=Sum("amount"))["total"]

        category_summary=all_incomes.values("category").annotate(total=Sum("amount"))

        data={

            "income_total":income_total,

            "category_summary":category_summary
        }

        return Response(data=data)

        

