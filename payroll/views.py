import calendar
from datetime import datetime
from django.shortcuts import render,redirect
from payroll.models import Payroll
from attendence.models import Attendence
from employee.models import Employee
from django.views.generic import View
from django.http import HttpResponse
from datetime import timedelta
import time
from datetime import date, timedelta
from datetime import datetime
from calendar import monthrange


# Create your views here.


   
class PayrollView(View):
	template_name='payroll/payroll.html'
	context_object_name="obj"
	
        
	def get(self,request):
		given_date=datetime.today().date()
		print(given_date)
		
	
		v_date=request.GET.get('date')
		print(v_date)
		print(type(v_date))
	

		x_date=datetime.strptime(v_date, '%Y-%m-%d')
		print(type(x_date))
		con_date=x_date.date()
		print(type(con_date))
	
		
		last_day_of_month=con_date.replace(day = monthrange(con_date.year, con_date.month)[1])
		print(type(last_day_of_month.day))
		
				
		first_day_of_month = con_date.strftime("%Y-%m-01")
		print(first_day_of_month)
		
		dt = datetime.today()
		print("ok")
		html="ok" 
		current_month=dt.month
		max_date=last_day_of_month.day

		res_sal=0
		total_days=0
		half_days=0
		leave=0
		v_empid = request.GET.get('employee_id')
		print('v_empid',v_empid)
		employees=Employee.objects.filter(id_number=v_empid) 
		print(employees)
		for e in employees:
			first_name=e.first_name
			employee_id=e.id
			print(first_name)
			print(employee_id)
			
  		
		attendences = Attendence.objects.values('signin_time','signout_time').filter(employee_id=employee_id,signin_time__gte=first_day_of_month, signout_time__lte=last_day_of_month)
		print('hello',type(attendences))
		print(attendences)
		

		total_hours=8
		no_of_days=0
		for sub in attendences:
			res=sub['signout_time']
			print(res)
			print('type',type(res))
			res1=sub['signin_time']
			print(res1)
			diff = res - res1
			days, seconds = diff.days, diff.seconds
			hours = days * 24 + seconds // 3600
			minutes = (seconds % 3600) // 60
			seconds = seconds % 60
			print(hours,minutes,seconds)
			working_hours = hours
			
			
			if working_hours >= total_hours:
				no_of_days=no_of_days+1
			

			elif working_hours < total_hours:
				no_of_days=no_of_days+0.5
				print(no_of_days)

		payrolls=Payroll.objects.filter(employee_id=employee_id).values('salary')	
		

		for j in payrolls:
			res_sal=j['salary']
			print(type(res_sal))
		
			
		print(payrolls)
		print(type(payrolls))
		
	
		v_salary=(res_sal/max_date) * no_of_days
		print(v_salary)
	
		

		v_html='''<html>
<head>
	<body>
		
		<h1>payroll generate</h1>
	
	
	<table>
	 	<thead>
			<th>Employee Name: {0}</th> 
			
			<th>Employee Id:{1}</th>
			
			<th>Working Hours:{2}</th>
			<th>Salary:{3}</th>
		</thead>
		
	</table>
		

		</body>
		</html>'''.format(first_name,employee_id,working_hours,v_salary)
		return HttpResponse(v_html)

		

			

























		
	
	



   



