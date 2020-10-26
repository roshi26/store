from django.urls import path, include
from customer import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('a/', views.CustomerListView.as_view(), name='product-list'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/register/',views.RegisterAPI.as_view(), name='register'),

    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/change-password/',views.ChangePasswordView.as_view(),name="change-password"),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('api/customer/', views.CustomerAPI.as_view(), name='customer'),
   
    path('api/cart/', views.CartView.as_view(), name='cart'),

    path('api/cartitem/', views.CartItemView.as_view(), name='cartitem'),

    path('api/cartitem/update/<int:pk>', views.CartItemUpdateView.as_view(), name='cart-update'),
    path('api/cartitem/delete/<int:pk>', views.CartItemUpdateView.as_view(), name='cart-delete'),



 






]


