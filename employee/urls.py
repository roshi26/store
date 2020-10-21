from django.urls import path
from employee import views

urlpatterns = [

   
    path('view/', views.EmployeeView.as_view(), name='EmployeeView'),
    path('list/',views.EmployeeList.as_view(),name='EmployeeList'),
    path('detail/<int:pk>',views.EmployeeDetail.as_view(), name='EmployeeDetail'),
    path('update/<int:pk>', views.EmployeeUpdate.as_view(), name='EmployeeUpdate'),
    path('delete/<int:pk>', views.EmployeeDelete.as_view(), name='EmployeeDelete')
    ]