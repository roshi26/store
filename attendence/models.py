from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee



class Attendence(models.Model):  
    designation = models.CharField(max_length=200, default="None",blank=True)
    signin_time = models.DateTimeField(blank=True)
    signout_time=models.DateTimeField(blank=True)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.designation