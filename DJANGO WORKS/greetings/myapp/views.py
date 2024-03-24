from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"goodmorning.html")

class HelloWorld(View):
    def get(self,request,*args,**kwargs):
        return render(request,"helloworld.html")

class GoodAfterNoon(View):
    def get(self,request,*args,**kwargs):
        return render(request,"afternoon.html")

class GoodEvening(View):
    def get(self,request,*args,**kwargs):
        return render(request,"evening.html")

class GoodNight(View):
    def get(self,request,*args,**kwargs):
        return render(request,"gdnyt.html")

class WelcomeDjango(View):
    def get(self,request,*args, **kwargs):
        return render(request,"welcome.html")

class SelfIntroView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"intro.html")

class BatchInfoView(View):

    def get(self,request,*args, **kwargs):
        data={
            "batch_name":"Python November",
            "students_count":45,
            "faculty":"Sajay"
        }
        return render(request,"batchinfo.html",data)

class CourseInfoView(View):

    def get(self,request,*args, **kwargs):
        data={
            "course_name":"python Django",
            "course_duration":"7month",
            "course_fee":3500
        }
        return render (request,"courseinfo.html",data)

class SachinView(View):

    def get(self,request,*args, **kwargs):
        data={
            "name":"Sachin Tendulkar",
            "role":"Cricketer",
            "age":50,
            "place":"mumbai",
            "born":"24 April 1973"
        }
        return render (request,"sachin.html",data)

class ChiefMinisterView(View):
    def get(self,request,*args,**kwargs):
        data={
            "name":"OOMMEN CHANDY",
            "role":"Former Chief Minister of Kerala",
            "born":"31 october 1943",
            "died":"18 july 2023",
            "party":"indian National Congress"
        }
        return render(request,"cm.html",data)



