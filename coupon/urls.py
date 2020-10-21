from django.urls import path
from coupon import views
urlpatterns = [

    path('view/', views.Coupon_view.as_view(), name='Coupon_view'),
    path('list/',views.Coupon_list.as_view(),name='Coupon_list'),
    path('coudetail/<int:pk>',views.Coupon_detail.as_view(), name='Coupon_detail'),
    path('couupdate/<int:pk>', views.Coupon_update.as_view(), name='Coupon_update'),
    path('coudelete/<int:pk>', views.Coupon_delete.as_view(), name='Coupon_delete')
    ]