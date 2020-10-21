from django.db import models
from employee.models import Employee
# Create your models here.

class Payroll(models.Model):
	salary=models.FloatField()
	gross_pay=models.FloatField()
	net_pay=models.FloatField()
	tax=models.FloatField()
	month=models.CharField(max_length=200, null=True, blank=True)
	year=models.DateField(auto_now_add=True, null=True, blank=True)
	created_at=models.DateField(auto_now_add=True, blank=True, null=True)
	modified_at=models.DateField(auto_now=True)
	employee=models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
	

	
	
