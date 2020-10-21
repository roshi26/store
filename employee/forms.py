from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields=['username','password','first_name','last_name','id_number','phone_number','job_title','department','location','start_date','end_date','created_by']
		widgets={
		'password':forms.PasswordInput(),
		}