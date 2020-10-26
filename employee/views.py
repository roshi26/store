from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View,ListView,DetailView
from django.views.generic.edit import  UpdateView, DeleteView, CreateView
from employee.models import Employee
from employee.forms import EmployeeForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy	
# Create your views here.


 

class EmployeeView(CreateView):
	model=Employee
	template_name='employee/employee_form.html'
	form_class=EmployeeForm


	def post(self,request):
		
		if request.method=="POST":
			form=EmployeeForm(request.POST)
			if form.is_valid():
				user=form.save()
				user.set_password(user.password)
				user.save()
				return HttpResponseRedirect('/employee/list')
			form=EmployeeForm()
		return render(request,'employee/employee_form.html',{'form':form})
	


class EmployeeList(ListView):
	model=Employee
	template_name='employee/employee_list.html'
	fields=['first_name','last_name','id_number','phone_number','job_title','department','email','location','start_date','end_date']
	context_object_name='employees'

	def get_queryset(self):
		return Employee.objects.filter(created_by=self.request.user)


class EmployeeDetail(DetailView):
	model=Employee
	template_name='employee/employee_detail.html'
	context_object_name='emp'


class EmployeeUpdate(UpdateView):
	model=Employee
	template_name='employee/employee_update.html'
	fields=['first_name','last_name','id_number','phone_number','job_title','department','email','location','start_date','end_date']
	success_url=reverse_lazy('EmployeeList')


class EmployeeDelete(DeleteView):
	model=Employee
	template_name='employee/employee_confirm_delete.html'
	success_url=reverse_lazy('EmployeeList')
