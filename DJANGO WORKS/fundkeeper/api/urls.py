from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("expenses",views.ExpenseViewSet,basename="expenses")

router.register("income",views.IncomeViewSet,basename="income")

urlpatterns = [
    
    path('register/',views.UserCreationView.as_view()),

    path('income/summary/',views.IncomeSummaryView.as_view()), #api view use chyumbol

    path('expenses/summary/',views.ExpenseSummaryView.as_view())

]+router.urls
