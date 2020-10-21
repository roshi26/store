from django.urls import path
from attendence import views

urlpatterns = [
    path('list/', views.EmployeeListView.as_view(),name='employee_list' ),
    path('<int:pk>/details/', views.EmployeeDetailView.as_view(), name="employee_details"),
    path('<int:pk>/update/', views.EmployeeUpdateView.as_view(), name="employee_update"),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name="employee_delete"),

    path('regis/', views.Registration.as_view(), name='employee_reg'), #first url
    path('login/', views.LoginView.as_view(), name="user_login"),
    path('logout/', views.LogoutView.as_view(), name="user_logout"),
    path('login/profile/', views.MyProfile.as_view(), name="my_profile"),

    path('signin/', views.SignInView.as_view(), name='sign_in'),
    path('view/', views.AttendenceView.as_view(), name="att"),
    path('signout/', views.SignoutView.as_view(), name="sign_out"),
    path('history/', views.AttendenceHistory.as_view(), name="history"),





    ]