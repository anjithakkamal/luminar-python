from django import forms 

from todo.models import Task

class TaskForm(forms.ModelForm):

    class Meta:

        model=Task

        exclude=("id","created_date")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "owner":forms.TextInput(attrs={"class":"form-control"}),
            
            

        }