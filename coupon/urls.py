from django.urls import path
from coupon import views
urlpatterns = [

    path('view/', views.CouponView.as_view(), name='Coupon_view'),
    path('list/',views.CouponList.as_view(),name='Coupon_list'),
    path('detail/<int:pk>',views.CouponDetail.as_view(), name='Coupon_detail'),
    path('update/<int:pk>', views.CouponUpdate.as_view(), name='Coupon_update'),
    path('delete/<int:pk>', views.CouponDelete.as_view(), name='Coupon_delete')
    ]