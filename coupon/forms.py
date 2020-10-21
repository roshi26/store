from django import forms
from coupon.models import Coupon
class CouponForm(forms.ModelForm):
	class Meta:
		model=Coupon
		fields="__all__"
	


