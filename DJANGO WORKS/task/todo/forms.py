from django import forms 

from todo.models import Task

from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):

    class Meta:

        model=Task

        exclude=("id","created_date")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "owner":forms.TextInput(attrs={"class":"form-control"}),   

        }

class RegistrationForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","email","password"]