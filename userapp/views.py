from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.urls import reverse
from userapp.forms import CustomUserCreationForm


# Create your views here.
def dashboard(request):
	return render(request, 'userapp/dashboard.html')


def register(request):
	if request.method=="GET":
		return render(
			request, "userapp/register.html",
			{"form":CustomUserCreationForm}
			)

	elif request.method=="POST":
		form=CustomUserCreationForm(request.POST)

		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect(reverse("user_dashboard"))
	return render(request, 'userapp/register.html')


def store(request):
	return render(request,'userapp/store.html')