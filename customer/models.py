from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from productapp.models import Product

class Customers(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	phone_number=models.IntegerField()
	location=models.CharField(max_length=200)
	


	def __str__(self):
		return self.location


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
       
        "Password Reset for {title}".format(title="Some website title"),
        
        email_plaintext_message,
      
        "noreply@somehost.local",
        
        [reset_password_token.user.email]
    )


class Cart(models.Model):
	date_created=models.DateTimeField(auto_now_add=True)
	customer=models.ForeignKey(Customers, on_delete=models.CASCADE)
	total_price=models.IntegerField(null=True, blank=True)


class CartItem(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	customers=models.ForeignKey(Customers, on_delete=models.CASCADE)
	quantity=models.IntegerField(null=True, blank=True)
	cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
	total_price=models.IntegerField(null=True, blank=True)








