from django.conf.urls import include,url
from userapp.views import dashboard,register,store

urlpatterns = [
    url(r"^dashboard/",dashboard, name="user_dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/",register,name="user_register"),
    url('landing page',store),


]