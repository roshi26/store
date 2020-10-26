from django.urls import path
from partner import views



urlpatterns = [
    path('login/', views.LoginView.as_view(), name="logins"),
    path('login/profile/', views.ProfileView.as_view(), name="profile"),
    path('logout/', views.LogoutView.as_view(), name="logouts"),
    path('registration/', views.PartnerView.as_view(), name="partners"), #first url to register





 

  


]


