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
	discount=models.IntegerField()	

	def __str__(self):
		return (self.name)



class Coupon(models.Model):
	
	expiry_date=models.DateField()
	coupon_number=models.IntegerField()
	issue_by=models.CharField(max_length=200)
	issue_to=models.CharField(max_length=200)
	created_by=models.CharField(max_length=200)
	recieve_by=models.CharField(max_length=200)
	product=models.ForeignKey(Product, on_delete=models.CASCADE)


	def __str__(self):
		return self.created_by

	


