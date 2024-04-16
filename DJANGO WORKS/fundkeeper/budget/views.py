from django.shortcuts import render,redirect

from django.views.generic import View

from budget.forms import ExpenseForm, IncomeForm

from budget.models import Expense,Income

from django.contrib import messages

from django.utils import timezone

from django.db.models import Sum

# Create your views here.

class ExpenseCreateView(View):

    def get(self,request,*args, **kwargs):

        form_instance=ExpenseForm()

        qs=Expense.objects.all()

        return render(request,"expense_add.html",{"form":form_instance,"data":qs})

    def post(self,request,*args, **kwargs):

        form_instance=ExpenseForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"expense created")

            print("expense has been created")

            return redirect('expense-add')
        
        else:

            messages.error(request,"error in creation")

            return render(request,"expense_add.html",{"form":form_instance})

class ExpenseUpdateView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        expense_object=Expense.objects.get(id=id)

        form_instance=ExpenseForm(instance=expense_object)

        return render(request,"expense_edit.html",{"form":form_instance})

    def post(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        expense_object=Expense.objects.get(id=id)

        form_instance=ExpenseForm(instance=expense_object,data=request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,'expense updated')

            return redirect('expense-add')
        
        messages.error(request,"error in updation")

        return render(request,"expense_edit.html",{"form":form_instance})

class ExpenseDetailView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        qs=Expense.objects.get(id=id)

        return render(request,"expense_detail.html",{"data":qs})

class ExpenseDeleteView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        Expense.objects.get(id=id).delete()

        messages.success(request,'expense deleted')

        return redirect('expense-add')

class ExpenseSummaryView(View):

    def get(self,request,*args, **kwargs):

        current_month=timezone.now().month

        current_year=timezone.now().year

        expense_list=Expense.objects.filter(created_date__month=current_month,created_date__year=current_year)

        expense_total=expense_list.values("amount").aggregate(total=Sum("amount"))

        print(expense_total)

        category_summary=expense_list.values("category").annotate(total=Sum("amount"))

        print(category_summary)

        priority_summary=expense_list.values("priority").annotate(total=Sum("amount"))

        print(priority_summary)

        return render(request,"expense_summary.html")


     

# ___________________income view_____________________

class IncomeCreatedView(View):

    def get(self,request,*args, **kwargs):

        form_instance=IncomeForm()

        qs=Income.objects.all()

        return render(request,"income_add.html",{"form":form_instance,"data":qs})

    def post(self,request,*args, **kwargs):

        form_instance=IncomeForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"income create successfully!!!")

            print("income has been created")

            return redirect('income-add')
        
        else:

            return render(request,"income_add.html",{"form":form_instance})

class IncomeUpdateView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        income_object=Income.objects.get(id=id)

        form_instance=IncomeForm(instance=income_object)

        return render(request,"income_edit.html",{"form":form_instance})

    def post(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        income_object=Income.objects.get(id=id)

        form_instance=IncomeForm(instance=income_object,data=request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"income update successfully!!!!!!!!")

            return redirect('income-add')
        
        messages.error(request,"error in updation")

        return render(request,"income_edit.html",{"form":form_instance})

class IncomeDetailView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        qs=Income.objects.get(id=id)

        return render(request,"income_detail.html",{"data":qs})

class IncomeDeleteView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        Income.objects.get(id=id).delete()

        messages.success(request,"income delete successfully!!!")

        return redirect('income-add')

class IncomeSummaryView(View):

    def get(self,request,*args, **kwargs):

        current_month=timezone.now().month

        current_year=timezone.now().year

        income_list=Income.objects.filter(created_date__month=current_month,created_date__year=current_year)

        income_total=income_list.values("amount").aggregate(total=Sum("amount"))

        print(income_total)

        category_summary=income_list.values("category").annotate(total=Sum("amount"))

        print(category_summary)

        return render(request,"expense_summary.html")


