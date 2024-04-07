from random import choices
from django import forms

class RegistrationForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()

    email=forms.EmailField()

class BmrForm(forms.Form):
    weight=forms.FloatField()

    height=forms.FloatField()

    age=forms.FloatField()

    options=(
        ("male","male"),
        ("female","female")
    )

    gender=forms.ChoiceField(choices=options)

    choices=(
        (1,"sedentary"),
        (2,"lightly Active"),
        (3,"Moderatively Active"),
        (4,"Very Active"),
        (5,"Extra Active")
    )

    activity_level=forms.ChoiceField(choices=choices)

class EmiForm(forms.Form):

    amount=forms.IntegerField()

    interest=forms.IntegerField()

    tenure=forms.IntegerField()

class TemperatureForm(forms.Form):

    temp_in_deg=forms.IntegerField(required=False)

    temp_in_fh=forms.IntegerField(required=False)

class ElectricityForm(forms.Form):

    previous_reading=forms.IntegerField()

    current_reading=forms.IntegerField()

    options=(
        (1,"single phase"),
        (2,"three phase")
    )

    phase=forms.ChoiceField(choices=options)