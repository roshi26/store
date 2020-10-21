from django.contrib.auth.forms import User
from partner.models import Partner
from django import forms
from django.contrib.auth.forms import UserCreationForm
class PartnerForm(UserCreationForm):
	class Meta:
		model=Partner
		fields=['username','first_name','last_name','email']

