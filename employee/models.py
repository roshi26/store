from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(User):

	id_number=models.IntegerField()
	phone_number=models.IntegerField()
	job_title=models.CharField(max_length=200)
	department=models.CharField(max_length=200)
	location=models.CharField(max_length=200)
	start_date=models.DateField()
	end_date=models.DateField()
	created_by=models.CharField(max_length=200, default="")


	