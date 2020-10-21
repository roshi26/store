from django.urls import path
from partner import views



urlpatterns = [
    path('login/', views.LoginView.as_view(), name="logins"),
    path('login/profile/', views.ProfileView.as_view(), name="profile"),
    path('logout/', views.LogoutView.as_view(), name="logouts"),
    path('partnerreg/', views.PartnerView.as_view(), name="partners"), #first url to register

    path('view/', views.EmployeeView.as_view(), name='employee_view'),
    path('elist/', views.EmployeeList.as_view(), name="emp_list"),
    path('detail/<int:pk>',views.EmployeeDetail.as_view(), name='employee_detail'),
    path('update/<int:pk>', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('delete/<int:pk>', views.EmployeeDelete.as_view(), name='employee_delete'),


    path('proview/', views.ProductView.as_view(), name='product_view'),
    path('prolist/', views.ProductList.as_view(), name="prod_list"),
    path('prodetail/<int:pk>',views.ProductDetail.as_view(), name='product_detail'),
    path('proupdate/<int:pk>', views.ProductUpdate.as_view(), name='product_update'),
    path('prodelete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),

    path('couview/', views.CouponView.as_view(), name='Coupon_view'),
    path('coulist/',views.CouponList.as_view(),name='Coupon_list'),
    path('coudetail/<int:pk>',views.CouponDetail.as_view(), name='Coupon_detail'),
    path('couupdate/<int:pk>', views.CouponUpdate.as_view(), name='Coupon_update'),
    path('coudelete/<int:pk>', views.CouponDelete.as_view(), name='Coupon_delete'),

    path('promview/', views.PromotionView.as_view(), name='promotions_view'),
    path('promlist/',views.PromotionList.as_view(),name='promotions_list'),
    path('promdetail/<int:pk>',views.PromotionDetail.as_view(), name='promotions_detail'),
    path('promupdate/<int:pk>', views.PromotionUpdate.as_view(), name='promotions_update'),
    path('promdelete/<int:pk>', views.PromotionDelete.as_view(), name='promotions_delete'),

]


