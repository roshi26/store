from django.urls import path
from attendence import views

urlpatterns = [
   
    path('detail/<int:pk>', views.EmployeeDetailView.as_view(), name="employee_detailed"),
    path('update/<int:pk>', views.EmployeeUpdateView.as_view(), name="employee_updated"),

    path('registration/', views.Registration.as_view(), name='employee_reg'), #first url
    path('login/', views.LoginView.as_view(), name="user_login"),
    path('logout/', views.LogoutView.as_view(), name="user_logout"),
    path('login/profile/', views.MyProfile.as_view(), name="my_profile"),

    path('signin/', views.SignInView.as_view(), name='sign_in'),
    path('view/', views.AttendenceView.as_view(), name="att"),
    path('signout/', views.SignoutView.as_view(), name="sign_out"),
    path('history/', views.AttendenceHistory.as_view(), name="history"),





    ]