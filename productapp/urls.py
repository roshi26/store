from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from productapp import views
urlpatterns = [
    path('view/', views.ProductView.as_view(), name='product_view'),
    path('list/',views.ProductListView.as_view(),name='product_list'),
    path('prodetail/<int:pk>',views.ProductDetailView.as_view(), name='product_detail'),
    path('proupdate/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('prodelete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete')
    ]