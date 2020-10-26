from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,DetailView, ListView, DeleteView, View
from django.views.generic.edit import UpdateView, CreateView, FormView
from django.urls import reverse_lazy
from attendence.forms import AttendenceForm
from employee.models import Employee
from attendence.models import Attendence
from django.contrib.auth.mixins import LoginRequiredMixin
from employee.forms import EmployeeForm
from datetime import datetime, timedelta
from datetime import date
import time


class Registration(FormView):
    template_name='employee/employee_attendence_registration.html'
    form_class=EmployeeForm

    
    def post(self,request):
        if request.method=="POST":
            form=EmployeeForm(request.POST)
            if form.is_valid():
                user=form.save()
                user.set_password(user.password)
                user.save()
            return HttpResponseRedirect('/attendence/login')
        else:
            form=EmployeeForm()
            my_dict={'form':form}
        return render(request,'employee/employee_attendence_registration.html')

 
class LoginView(TemplateView):
    model=Attendence
    template_name='attendence/login.html'
    redirect_field_name='profile'

    def get(self,request):
        return render(request,'attendence/login.html')

    
    def post(self,request):
    
        
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('profile')
            else:
                state="inactive"
        return render(request,'attendence/login.html',{'state':state})



class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return render(request,'attendence/login.html')

    

class EmployeeDetailView(LoginRequiredMixin,DetailView):
    model=Employee
    login_url='/login/'
    template_name='employee/emp_attendence_detail.html'
    context_object_name='user'



class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model=Employee

    login_url='/login/'
    fields=['first_name','last_name','phone_number','job_title','email','location']

    template_name='employee/emp_attendence_update.html'
    context_object_name="user"
    


    
    def get_success_url(self):
        
        employee_details=self.kwargs['pk']
        return reverse_lazy('employee_detailed',kwargs={'pk':self.object.pk})



class MyProfile(LoginRequiredMixin,DetailView):
    model=  Attendence
    form_class=AttendenceForm
    login_url='/login/'
    template_name = 'attendence/profile.html'

    def get_object(self):
        return self.request.user

  

class AttendenceView(View):
    model=Employee
    template_name='attendence/attendence_data.html'
        



    def get(self,request):
        y=Attendence.objects.values('signin_time').filter(employee=request.user)
        print('hello',y)
        context={'y':y}
        return render(request,'attendence/attendence_data.html',{'y':y})



class SignInView(LoginRequiredMixin,TemplateView):
    model=Attendence
    login_url='/login/'
    template_name='attendence/signin.html'
    success_url=reverse_lazy('att')
    context_object_name="sign"



class SignoutView(LoginRequiredMixin,TemplateView):
    model=Attendence
    template_name='attendence/signout.html'
    login_url='/login/'
    success_url=reverse_lazy('user_login')



class AttendenceHistory(View):
    model=Attendence
    template_name='attendence/attendence_history.html'
      

    def get(self,request):
        v_date=datetime.now()
        x=Attendence.objects.values('signin_time','signout_time').filter(employee=request.user)
        print(x)
        context={'x':x}
        return render(request,'attendence/attendence_history.html',{'x':x})
