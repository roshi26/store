from django.db import models

# Create your models here.
class Product(models.Model):
	name=models.CharField(max_length=200, null=True, blank=True)
	created_at=models.CharField(max_length=200, null=True, blank=True)
	price=models.IntegerField()
	quality=models.IntegerField()
	issue_by=models.CharField(max_length=200, null=True, blank=True)
	issue_to=models.CharField(max_length=200,null=True, blank=True)
	last_updated=models.DateField(auto_now_add=True)
	brand=models.CharField(max_length=200, null=True, blank=True)
	quantity=models.IntegerField()
	coupon=models.CharField(max_length=200, null=True, blank=True)
	discount=models.IntegerField()
	created_by=models.CharField(max_length=200, default="")


	def __str__(self):
		return self.name

	




  