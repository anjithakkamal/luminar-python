from django import forms

class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    director=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    run_time=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border-info"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    producer=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))