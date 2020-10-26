from django.urls import path
from promotions import views

urlpatterns = [
    path('view/', views.PromotionView.as_view(), name='promotions_view'),
    path('list/',views.PromotionList.as_view(),name='promotions_list'),
    path('detail/<int:pk>',views.PromotionDetail.as_view(), name='promotions_detail'),
    path('update/<int:pk>', views.PromotionUpdate.as_view(), name='promotions_update'),
    path('delete/<int:pk>', views.PromotionDelete.as_view(), name='promotions_delete'),

    ]