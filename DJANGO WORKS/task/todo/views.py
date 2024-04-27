from itertools import count
from django.shortcuts import render,redirect

from django.views.generic import View

from todo.forms import TaskForm,RegistrationForm,LoginForm

from todo.models import Task

from django.contrib import messages

from django.utils import timezone

from django.db.models import Count

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

# Create your views here.

class TaskCreateView(View):

    def get(self,request,*args, **kwargs):

        form_instance=TaskForm()

        qs=Task.objects.filter(user_object=request.user)

        return render(request,"task_create.html",{"form":form_instance,"data":qs})

    def post(self,request,*args, **kwargs):

        form_instance=TaskForm(request.POST)

        if form_instance.is_valid():

            form_instance.instance.user_object=request.user

            form_instance.save()

            messages.success(request,"task added successfully!!!!!!!!")

            print("task has been created")

            return redirect('task-add')
        
        else:

            messages.error(request,"task adding error")

            return render(request,"task_create.html",{"form":form_instance})

class TaskUpdateView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        task_object=Task.objects.get(id=id)

        form_instance=TaskForm(instance=task_object)

        return render(request,"task_edit.html",{"form":form_instance})

    def post(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        task_object=Task.objects.get(id=id)

        form_instance=TaskForm(instance=task_object,data=request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"task updated successfully!!")

            return redirect('task-add')
        
        messages.error(request,"updating error")

        return render(request,"task_edit.html",{"form":form_instance})

class TaskDetailView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        qs=Task.objects.get(id=id)

        return render(request,"task_detail.html",{"data":qs})

class TaskDeleteView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        Task.objects.get(id=id).delete()

        messages.success(request,"task delete successfully!!!")

        return redirect('task-add')

class TaskSummaryView(View):

    def get(self,request,*args, **kwargs):
            
        current_month=timezone.now().month

        current_year=timezone.now().year

        task_list=Task.objects.filter(created_date__month=current_month,created_date__year=current_year,user_object=request.user)

        task_summary=task_list.values("status").annotate(count=Count("status"))

        print(task_summary)

        data={

            "task_summary":task_summary

            }

        return render(request,"task_summary.html",data)

class SignUpView(View):

    def get(self,request,*args, **kwargs):

        form_instance=RegistrationForm()

        return render(request,"register.html",{"form":form_instance})

    def post(self,request,*args, **kwargs):

        form_instance=RegistrationForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data)

            print("user create object successfully!!!")

            return redirect('signin')

        else:

            print("user creation error!!!!!!!")

            return render(request,'register.html',{"form":form_instance})

class SignInView(View):

    def get(self,request,*args, **kwargs):

        form_instance=LoginForm()

        return render(request,"login.html",{"form":form_instance})

    def post(self,request,*args, **kwargs):

        form_instance=LoginForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                return redirect('task-add')
        
        messages.error(request,"invalid credential")

        return render(request,"login.html",{"form":form_instance})

class SignOutView(View):

    def get(self,request,*args, **kwargs):

        logout(request)

        return redirect('signin')


