from django.conf.urls import include,url
from userapp.views import dashboard,register

urlpatterns = [
    url(r"^dashboard/",dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/",register,name="register"),
  


]