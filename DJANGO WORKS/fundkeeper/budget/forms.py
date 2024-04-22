
from django import forms

from budget.models import Expense,Income

from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):

    class Meta:

        model=Expense

        exclude=("id","created_date")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "amount":forms.NumberInput(attrs={"class":"form-control"}),

            "category":forms.Select(attrs={"class":"form-control form-select"}),

            "owner":forms.TextInput(attrs={"class":"form-control"}),

            "priority":forms.Select(attrs={"class":"form-control form-select"})

        }


class IncomeForm(forms.ModelForm):

    class Meta:

        model=Income

        exclude=("id","created_date")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "amount":forms.NumberInput(attrs={"class":"form-control"}),

            "category":forms.Select(attrs={"class":"form-control form-select"}),

            "owner":forms.TextInput(attrs={"class":"form-control"})

        }

class RegistrationForm(forms.ModelForm):

    class Meta:

        model=User
        
        fields=["username","email","password"]

class LoginForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()
       