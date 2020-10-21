from django.urls import path
from payroll import views


urlpatterns = [
    path('payroll/', views.PayrollView.as_view(), name="payrolls")



]