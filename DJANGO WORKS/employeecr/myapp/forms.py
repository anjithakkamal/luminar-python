from django import forms

class EmployeeForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border border-info"}))

    location=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control border border-info"}))

    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    