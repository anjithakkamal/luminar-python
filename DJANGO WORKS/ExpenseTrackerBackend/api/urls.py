from django.urls import path

from api import views

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("expense",views.ExpenseViewSetView,basename="expense")


urlpatterns=[
path('token/',TokenObtainPairView.as_view()),

path('token/refresh/',TokenRefreshView.as_view()),
]+router.urls