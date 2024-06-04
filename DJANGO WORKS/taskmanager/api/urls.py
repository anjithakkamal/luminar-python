from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("employee",views.EmployeeViewSetView,basename="employee")

urlpatterns = [
    
]+router.urls
