from django import forms
from promotions.models import Promotions


class PromotionsForm(forms.ModelForm):
	class Meta:
		model=Promotions
		fields="__all__"