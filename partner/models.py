from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Partner(User):
	phone_number=models.IntegerField(null=True, blank=True)
	created_at=models.DateField(auto_now_add=True)
	modified_at=models.DateField(auto_now=True)










