from django.db import models

# Create your models here.
class Promotions(models.Model):
	DAYS=(
	('m', 'Monday'),
	('t','Tuesday'),
	('w','Wednesday'),
	('t','Thursday'),
	('f', 'Friday'),
	('s','Saturday'),
	('sn','Sunday'),
	)
	
	day=models.CharField(choices=DAYS, max_length=20)
	created_at=models.DateField(auto_now_add=True)
	modified_at=models.DateField(auto_now=True)
	created_by=models.CharField(max_length=200)
	modified_by=models.CharField(max_length=200)
